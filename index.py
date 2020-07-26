from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date
from apscheduler.schedulers.tornado import TornadoScheduler
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop, PeriodicCallback
from pgsql import cur

# sched = BlockingScheduler()
# sched.add_job(job, 'date', run_date=datetime(2020, 7, 26, 19, 31, 50), id='11')
# print(sched.get_jobs())
# sched.start()

scheduler = None
job_ids = []


def job(options):
    print(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'), 123, options, 123)


def init_scheduler():
    global scheduler
    scheduler = TornadoScheduler()
    scheduler.start()


class MainHandler(RequestHandler):
    def get(self):
        self.write(
            '<a href="/scheduler?job_id=1&action=add">add job</a><br><a href="/scheduler?job_id=1&action=remove">remove job</a>')


class SChedulerHandler(RequestHandler):
    def get(self):
        global job_ids
        job_id = self.get_query_argument('job_id', None)
        action = self.get_query_argument('action', None)
        if job_id:
            if 'add' == action:
                if job_id not in job_ids:
                    job_ids.append(job_id)
                    scheduler.add_job(job, 'interval', seconds=5, id=job_id, args=(job_id,))
                    self.write('add success')
                else:
                    self.write('exists')
            elif 'remove' == action:
                if job_id in job_ids:
                    scheduler.remove_job(job_id)
                    job_ids.remove(job_id)
                    self.write('remove success')
                else:
                    self.write('exists')
        else:
            self.write('缺少参数')


if __name__ == '__main__':
    routes = [
        (r'/', MainHandler),
        (r'/scheduler/?', SChedulerHandler),
    ]
    init_scheduler()
    app = Application(routes, debug=True)
    app.listen(30000,'localhost')
    IOLoop.current().start()
