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
        print 'Now I am doing my job (%s) with para %s' % (self.__name, para)

    def start_schedule_task(self):
        para = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        schedule.every(30).seconds.do(self.do_task, para)
        while True:
            schedule.run_all(5)

    def start_backend_schedule(self):
        threading.Thread(target=self.start_schedule_task).start()


task = Task()


