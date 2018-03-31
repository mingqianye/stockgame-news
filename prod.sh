#!/bin/bash
docker build . -t news-server && docker run -it --rm -p 5000:5000 news-server
