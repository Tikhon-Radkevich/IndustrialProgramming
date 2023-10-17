# shellcheck disable=SC2086
# shellcheck disable=SC2046

# run gui
#docker start condescending_raman
#docker exec -it condescending_raman sh -c "mkdir /app/cache"
docker run -it -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm pp-app gui
