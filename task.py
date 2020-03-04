#!/usr/bin/python
# -*- coding: utf-8 -*-
import schedule
import time
import threading


class Task(object):
    def __init__(self):
        self.__name = "Task Example"
        print 'Task init and start schedule'

    def do_task(self, para):
        pit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print 'Now I am doing my job (%s) with para (%s) at %s' % (self.__name, para, pit)

    def start_schedule_task(self):
        schedule.every(30).seconds.do(self.do_task, "whatever parameters")
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_backend_schedule(self):
        threading.Thread(target=self.start_schedule_task).start()


task = Task()


