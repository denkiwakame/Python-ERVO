# Python-ERVO

![demo](https://user-images.githubusercontent.com/1871262/102694198-e0c27280-4262-11eb-89df-d1064529c5be.gif)![demo2](https://user-images.githubusercontent.com/1871262/102694194-db652800-4262-11eb-8a4e-eecb57c167ac.gif)

- This repository containts the code for interactive crowd simulator used in the IROS 2020 paper ["L2B: Learning to Balance the Safety-Efficiency Trade-off in Interactive Crowd-aware Robot Navigation"](https://arxiv.org/pdf/2003.09207.pdf)
- The original RVO implementation is the folk of [Python bindings for Optimal Reciprocal Collision Avoidance](https://github.com/sybrenstuvel/Python-RVO2).


### Dependencies
- CMake `3.1+`
- Cython `0.21.1+`

### Setup

```sh
$ pip install -r requirements.txt
$ python setup.py build      # build
$ python setup.py install    # build & install
```

### Usage
- For more details, see `example_ervo.py`

```python
# original RVO
sim_rvo = rvo2.PyRVOSimulator(time_step, *params, radius, max_speed)
sim_rvo.doStep()

# extended ERVO
sim_ervo = rvo2.PyERVOSimulator(time_step, *params, radius, max_speed)
sim_ervo.doStep((beep_agent.px, beep_agent.py), beep_radius)
```

### Citation
If you find the simulator useful for your research, please consider citing:

```
@inproceedings{nishimura2020l2b,
  title={L2B: Learning to Balance the Safety-Efficiency Trade-off in Interactive Crowd-aware Robot Navigation},
  author={Nishimura, Mai and Yonetani, Ryo},
  journal={IEEE/RSJ International Conference on Intelligent Robots and Systems},
  year={2020},
  publisher={IEEE}
}

@incollection{van2011reciprocal,
  title={Reciprocal n-body collision avoidance},
  author={Van Den Berg, Jur and Guy, Stephen J and Lin, Ming and Manocha, Dinesh},
  booktitle={Robotics research},
  pages={3--19},
  year={2011},
  publisher={Springer}
}
```
