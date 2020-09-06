# tiny_flask_app
tiny flask app to test development using docker


$ sudo docker build -t tiny_flask_app .


$ sudo docker run -it --rm -p 4040:4040 --mount type=bind,source="$(pwd)"/,target=/usr/src/app/ --name tiny_flask_app_running tiny_flask_app


