#!/usr/bin/env python

import os
import sys
import logging

try:
    import psycopg2 as pg
    import psycopg2.extras
except:
    print("Install psycopg2")
    exit(123)

import json

import logging
logger = logging.getLogger()


data_dir = "data.json"

DB_HOST = "localhost"
DB_NAME = "TDD-test"
DB_USER = "postgres"
DB_PASS = "123"
dbconn = pg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

logger.info("Loading data from '{}'".format(data_dir))

cursor = dbconn.cursor()

counter = 0
empty_files = []

class ProgressInfo:

    def __init__(self, dir):
        files_no = 0
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".json"):
                    files_no += 1
        self.files_no = files_no
        print("Found {} files to process").format(self.files_no)

    def update(self, counter):
        self.bar.update(counter)

pi = ProgressInfo(os.path.expanduser(data_dir))

for root, dirs, files in os.walk(os.path.expanduser(data_dir)):
    for f in files:
        fname = os.path.join(root, f)

        if not fname.endswith(".json"):
            continue
        with open(fname) as js:
            data = js.read()
            if not data:
                empty_files.append(fname)
                continue
            import json
            dd = json.loads(data)
            counter += 1
            pi.update(counter)
            cursor.execute("""
                            INSERT INTO stats_data(data)
                            SELECT %s
                            WHERE NOT EXISTS (SELECT 42
                                              FROM stats_data
                                              WHERE
                                                    ((data->>'metadata')::json->>'country')  = %s
                                                AND ((data->>'metadata')::json->>'installation') = %s
                                                AND tstzrange(
                                                        to_timestamp((data->>'start_ts')::double precision),
                                                        to_timestamp((data->>'end_ts'  )::double precision)
                                                    ) &&
                                                    tstzrange(
                                                        to_timestamp(%s::text::double precision),
                                                        to_timestamp(%s::text::double precision)
                                                    )
                                             )
                        """, (data, str(dd['metadata']['country']), str(dd['metadata']['installation']), str(dd['start_ts']), str(dd['end_ts'])))

print("")

logger.debug("Refreshing materialized views")
cursor.execute("""REFRESH MATERIALIZED VIEW sessions""")
cursor.execute("""ANALYZE""")
dbconn.commit()

logger.info("Loaded {} files".format(counter))
logger.info("Found {} empty files".format(len(empty_files)))
if empty_files:
    logger.info("Empty files:")
    for f in empty_files:
        logger.info(" >>> {}".format(f))