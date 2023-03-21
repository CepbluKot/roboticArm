import logging, datetime


logging.basicConfig(level=logging.INFO, filename="logs/logfile_" + str(datetime.datetime.now()) +".log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
