import flask
import time
import os

from croniter import croniter
from datetime import datetime


app = flask.Flask(__name__)


def setup_cron_jobs():
    os.popen("crontab -r")
    cronjobs = []
    for filename in os.listdir("./cronjobs"):
        with open(
            os.path.join("./cronjobs", filename), "r"
        ) as f:  # open in readonly mode
            lines = f.readlines()
            for line in lines:
                if line.startswith("# cron: "):
                    cronjobs.append(
                        {
                            "cron": line.split("# cron: ", 1)[1].strip(),
                            "command": f"python3 ./cronjobs/{filename}",
                        }
                    )
                    break

    with open("crontab.tmp", "w") as f:
        for cronjob in cronjobs:
            f.write(f"{cronjob['cron']} {cronjob['command']}\n")

    os.popen("crontab crontab.tmp")
    time.sleep(1)  # sleep to let the file be processed
    os.remove("crontab.tmp")


cronjobs_ready = setup_cron_jobs()


def parse_crontab_list(output):
    if output.startswith("no crontab for"):
        return []

    cronjobs = []
    for line in output.splitlines():
        line_split = line.split(" ")
        time = " ".join(line_split[:5])
        cronjobs.append(
            {
                "time": time,
                "nextRun": croniter(time).get_next(datetime),
                "command": " ".join(line_split[5:]),
            }
        )

    return cronjobs


@app.route("/")
def index():
    crontab_list_command = os.popen("crontab -l")

    cronjobs = parse_crontab_list(crontab_list_command.read())
    return flask.render_template("index.html", cronjobs=cronjobs)
