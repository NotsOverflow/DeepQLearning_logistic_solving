#
#
#              _            _
# |\| _ _|_ _ / \    _  ___|_ |  _
# | |(_) |__> \_/\_/(/_ |  |  | (_)\^/
#
# macdo.py created December 1st 2020
# by richard juan (contact@richardjuan-business.com)
#
#
#

import random
import os
from copy import copy, deepcopy

class MacDo:
    def __init__(self):
        os.system('cls')
        self.day = 0.0
        self.action_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.reset()

    def render(self, mode='human', clean=True):
        if clean:
            os.system('cls')
        t = round(self.h * 100, 1)
        j = int(self.d * 10)
        f = True if self.ferier == 1.0 else False
        beau = int(self.beau * 100)
        ybm = int(self.ybm * 100)
        obm = int(self.obm * 100)
        vobm = int(self.vobm * 100)
        ymch = int(self.ymch * 100)
        omch = int(self.omch * 100)
        vomch = int(self.vomch * 100)
        ys = int(self.ys * 100)
        osp = int(self.os * 100)
        vos = int(self.vos * 100)
        trash = int(self.trashed * 100)
        r = self.lastReward
        tr = self.totalReward
        dd = self.done
        c = int(self.clients * 100)
        route = int(self.route * 100)
        print("**********************************************************************")
        print("\n--------------------------[environement]------------------------------")
        print("\n\tday: [%s] time: [%s] holyday: '%s' " % (j,t,f))
        print("\n\tweather: [%s] trafic: [%s]" % (beau, route))
        print("\n------------------------------[room]----------------------------------")
        print("\n\tnew bm:\t%s\tbm:\t%s\tcold bm:\t%s    " % (ybm,obm,vobm))
        print("\tnew ch:\t%s\tch:\t%s\tcold ch:\t%s    " % (ymch,omch,vomch))
        print("\tnew sp:\t%s\tsp:\t%s\tcold sp:\t%s       " % (ys,osp,vos))
        print("\n\ttotal clients: %s" % c)
        print("\n-----------------------------[results]--------------------------------")
        print("\n\tnot served clients: (%s)    trashed burgers: (%s)" % (self.no_burger, trash))
        print("\n\treward: (%s) total reward : (%s) done: '%s'" % (r, tr, dd))
        print("\n**********************************************************************")

    def reset(self):
        # day by beau, route, clients, d, h, burger, ferier
        self.done = False
        self.no_burger = 0
        self.trashed = 0.00
        self.totalReward = 0
        self.lastReward = 0
        self.beau, self.route, self.clients, self.d, self.h, self.burger, self.ferier = self.check_day_rdn(d=self.day)
        self.ymch, self.omch, self.vomch = 0.05, 0.00, 0.00
        self.ybm, self.obm, self.vobm = 0.05, 0.00, 0.00
        self.ys, self.os, self.vos = 0.05, 0.00, 0.00
        self.obs = [self.beau, self.route, self.clients, self.d, self.h, self.burger, self.ferier, self.ymch, self.omch, self.vomch, self.ybm, self.obm, self.vobm, self.ys, self.os, self.vos]
        return deepcopy(self.obs)

    def set_day(self, day=0.0):
        self.day = day

    def is_done(self):
        if self.h >= 0.20:
            self.done = True
            return True
        if self.clients >= 0.5:
            self.done = True
            return True
        return False

    def sell_burger(self):
        burger = self.gen_next_burger(self.ferier, self.h) if self.chances(40) else round(random.uniform(0.0, 1.0), 1)
        # bigmac
        if burger <= 0.3:
            if self.vobm <= 0.00:
                self.vobm = 0.00
                if self.obm <= 0.00:
                    self.obm = 0.00
                    if self.ybm <= 0.00:
                        self.ybm = 0.00
                        return False
                    else:
                        self.ybm = round(self.ybm - 0.01, 3)
                else:
                    self.obm = round(self.obm - 0.01, 3)
            else:
                self.vobm = round(self.vobm - 0.01,3)
        elif burger <= 0.6:
            if self.vomch <= 0.00:
                self.vomch = 0.00
                if self.omch <= 0.00:
                    self.omch = 0.00
                    if self.ymch <= 0.00:
                        self.ymch = 0.00
                        return False
                    else:
                        self.ymch = round( self.ymch - 0.01, 3)
                else:
                    self.omch = round( self.omch - 0.01, 3)
            else:
                self.vomch = round( self.vomch - 0.01, 3)
        else:
            if self.vos <= 0.00:
                self.vos = 0.00
                if self.os <= 0.00:
                    self.os = 0.00
                    if self.ys <= 0.00:
                        self.ys = 0.00
                        return False
                    else:
                        self.ys = round(self.ys - 0.01, 3 )
                else:
                    self.os = round(self.os - 0.01, 3 )
            else:
                self.vos = round(self.vos - 0.01, 3 )
        self.clients = round( self.clients - 0.01, 3)
        return True

    def step(self, action):
        reward = 1000

        self.trashed = round(self.vomch + self.vobm + self.vos, 3)

        reward -= self.vomch *10000
        self.vomch = self.omch
        self.omch = self.ymch
        self.ymch = 0.00

        reward -= self.vobm *10000
        self.vobm = self.obm
        self.obm = self.ybm
        self.ybm = 0.00
        
        reward -= self.vos *10000
        self.vos = self.os
        self.os = self.ys
        self.ys = 0.00

        if action <= 10:
            self.ybm = round(self.ybm + (0.03 * action), 2)
        elif action <= 20:
            self.ymch = round(self.ymch+ (0.03 * (action%10)), 2)
        else:
            self.ys = round(self.ys + (0.03 * (action%10)),2)

        clients = int(self.clients * 100)
        self.no_burger = 0
        for _ in range(clients):
            if not self.sell_burger():
                self.no_burger += 1
        reward -= self.no_burger * 100 * 2
        reward -= round(self.clients * 1000 * 2,0)
        if self.clients <= 0.00:
            self.clients = 0.00
            reward += 1000
        elif self.clients >= 0.45:
            reward -= 15000
        reward = int(reward)
        self.h = round(self.h + 0.001, 3)
        self.obs = [self.beau, self.route, self.clients, self.d, self.h, self.burger, self.ferier, self.ymch, self.omch, self.vomch, self.ybm, self.obm, self.vobm, self.ys, self.os, self.vos] #16
        self.lastReward = reward
        self.totalReward += reward
        self.clients = round(self.clients + self.gen_next_hour(self.d, self.h, self.ferier, self.beau, self.route), 2 )
        return deepcopy(self.obs), reward, self.is_done(), {"totalReward":self.totalReward}


    def gen_next_hour(self,d=0.0,h=0.08,ferier=0.0,beau=0.7,route=0.3):
        clients = ( 5*beau ) + (5-(5*route)) + random.randint(0, 3)
        if ferier == 1.0:
            clients += 3
        if (h >= 0.11 and h <= 0.13) or (h >= 0.18 and h <= 0.20):
            clients += 3
        if d >= 0.5 and d <= 0.7:
            clients += 1
        return round(clients * 0.01, 2)

    def gen_next_burger(self, ferier=0.0, h=0.08):
        burger = 0.0
        if ferier == 1.0:
            burger = 1.0
        else:
            if (h >= 0.11 and h <= 0.13) or (h >= 0.18 and h <= 0.20):
                burger = 0.1
            else:
                burger = round(random.uniform(0.0, 1.0), 1)
        return round( burger, 1)


    def check_day_rdn(self, d=0.0, h=0.08, ferier=None):
        if d >= 0.7:
            d = 0.7
        elif d <= 0.0:
            d = 0.0
        if not ferier:
            ferier = 1.0 if self.chances(10) else 0.0
        beau = round(random.uniform(0.1, 0.3), 1) if self.chances(20) else round(random.uniform(0.5, 1.0), 1)
        route = round(random.uniform(0.1, 0.3), 1) if self.chances(80) else round(random.uniform(0.5, 1.0), 1)

        clients = self.gen_next_hour(d, h, ferier, beau, route)
        burger = self.gen_next_burger(ferier, h)
        

        return beau, route, clients, d, h, burger, ferier
    
    def chances(self, p=100):
        return True if random.randint(0, 100) < p else False

