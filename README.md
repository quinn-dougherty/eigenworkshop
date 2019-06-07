# eigenworkshop

Animations for a Lambda School After Hours workshop on decomposition.

# usage

Have at least 3 Gigabytes available. The image is under 2, but you'll be writing
video. 

``` shell
you:$ docker build -t eigenworkshop .
you:$ docker run -it -v $(pwd):/manim/ eigenworkshop
root@container:# cd manim
root@container:# manim ltrans-notes.py TransformInfiniteGrid
```

