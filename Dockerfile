FROM quinnd/manimlib-env:latest

RUN mkdir manim

COPY . /manim

ENTRYPOINT ["/bin/bash"]
