#!/usr/bin/env python

"""
minimal example of PyERVOSimulator
Author: Mai Nishimura <mai.nishimura@sinicx.com> <denkivvakame@gmail.com>
Copyright: 2020 OMRON SINIC X
"""

import numpy as np
import matplotlib.pyplot as plt
import rvo2


class Agent():
    def __init__(self, px, py, gx, gy, color):
        self.px = px
        self.py = py
        self.gx = gx
        self.gy = gy
        self.vx = 0
        self.vy = 0
        self.v_pref = 1.0
        self.color = color


class ERVO():
    def __init__(self):
        self.name = 'ERVO'
        self.safety_space = 0
        self.neighbor_dist = 10
        self.max_neighbors = 10
        self.time_horizon = 5
        self.time_horizon_obst = 5
        self.radius = 0.3
        self.max_speed = 1
        self.time_step = 0.25
        self.sim = None

        self.agents = [
            Agent(-3, -2.5, 3, 3, 'slategray'),
            Agent(0, -3.7, 0, 3, 'coral'),
            Agent(3, -3, -3, 3, 'slategray'),
        ]

    def step(self, beep=-1):
        if self.sim is None:
            params = self.neighbor_dist, self.max_neighbors, self.time_horizon, self.time_horizon_obst
            self.sim = rvo2.PyERVOSimulator(
                self.time_step, *params, self.radius, self.max_speed)
            for idx, agent in enumerate(self.agents):
                self.sim.addAgent((agent.px, agent.py), *params,
                                  self.radius, self.max_speed, (agent.vx, agent.vy))

        for idx, agent in enumerate(self.agents):
            velocity = np.array((agent.gx - agent.px, agent.gy - agent.py))
            speed = np.linalg.norm(velocity)
            pref_vel = velocity / speed if speed > 1 else velocity
            self.sim.setAgentPrefVelocity(idx, tuple(pref_vel))

        self.sim.doStep((self.agents[1].px, self.agents[1].py), beep)

        for idx, agent in enumerate(self.agents):
            agent.px, agent.py = self.sim.getAgentPosition(idx)
            agent.vx, agent.vy = self.sim.getAgentVelocity(idx)


def main():
    sim = ERVO()
    plt.figure(figsize=(2, 2))

    for i in range(200):
        if i > 13 and i < 16:
            sim.step(beep=1)
            plt.scatter(sim.agents[1].px, sim.agents[1].py,
                        s=500, marker='o', color=sim.agents[1].color, facecolor='none')
        else:
            sim.step(beep=-1)
        for agent in sim.agents:
            plt.scatter(agent.px, agent.py, color=agent.color)

        plt.xlim([-4.0, 4.0])
        plt.ylim([-4.0, 4.0])
        plt.waitforbuttonpress()
        plt.savefig(f"img/{i:02}.png")
        plt.clf()


if __name__ == '__main__':
    main()
