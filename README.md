# Crontab framework

This project helps you run in a simple way python cronjobs. Create all your automation in the folder `cronjobs`. They will be processed and set up with crontab automatically.

This project is inspired by [Hubot](https://hubot.github.com/).

## Run locally

- Create a python virtual environment
- Run: `FLASK_APP=app FLASK_DEBUG=1 flask run`
- http://127.0.0.1:5000/

![image](https://user-images.githubusercontent.com/2707508/148839368-6f15dc68-39a2-4844-893a-6558daa3193e.png)


## Add a new cronjob

- Create a new file in the folder `cronjobs`
- Prefix the automation with: `# cron: * * * * *` (replace with the correct time)
- Code & deploy the app with the script. The automation will be picked by the framework and deployed automatically.
