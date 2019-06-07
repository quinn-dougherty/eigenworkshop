# eigenworkshop

Animations for a Lambda School After Hours workshop on decomposition.

# usage

Have at least 3 Gigabytes available. The image is under 2, but you'll be writing
video. 

`clone` and `cd` into this repo, then

``` shell
you:$ docker build -t eigenworkshop .
you:$ docker run -it -v $(pwd):/manim/ eigenworkshop
root@container:# cd manim
root@container:# manim loop-transfo.py Symmetric 
```

This is based on Ubuntu. If OSx syntax is different, it'd be something minor. 

Windows users: I'm sorry, I don't know _anything_ about windows. 
