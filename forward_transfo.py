#!/usr/bin/env python

from manimlib.imports import *
from numpy.linalg import eigh, eig, inv
from numpy import matmul, diag, array, sqrt, exp, pi, sin, cos
from numpy.testing import assert_almost_equal

class ForwardDecomp(LinearTransformationScene):
    CONFIG = {
        "transposed_matrix" : [[0, 0], [0, 0]],

        "include_background_plane" : True,
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_WIDTH,
            "y_radius" : FRAME_HEIGHT,
        },
        "show_basis_vectors" : True
    }

    def construct(self):
        self.setup()
        self.loop(2, unit_time=3/4)

        # loops =2
        #for p in range(loops):
        #    lo = exp(-9.5-p)
        #    try:
        #        self.run(lag_order=lo)
        #    except Exception as e:
        #        raise e
    def isomorphism(self, A):
        eigenvalues, eigenvectors = eig(A)
        P = eigenvectors
        Lambda = diag(eigenvalues)
        P_inv = inv(eigenvectors)
        return P, Lambda, P_inv

    def run(self, time_unit=1, lag_order=10**-4):
        init = self.init(runtime=exp(-1))
        self.play(init)
        self.wait(exp(-3))

        A_inv = inv(self.transposed_matrix)
        P, Lambda, P_inv = self.isomorphism(self.transposed_matrix)

        self.apply_transposed_matrix(self.transposed_matrix, run_time=time_unit*3, lag_ratio=lag_order)
      
        #self.remove(init)
        self.apply_transposed_matrix(A_inv, run_time=exp(-2), lag_ratio=1)
        #self.play(init)

        self.apply_transposed_matrix(P, run_time=time_unit, lag_ratio=lag_order)
        self.apply_transposed_matrix(Lambda, run_time=time_unit, lag_ratio=lag_order)
        self.apply_transposed_matrix(P_inv, run_time=time_unit, lag_ratio=lag_order)


        #self.remove(init)
        self.apply_transposed_matrix(A_inv, run_time=exp(-2), lag_ratio=1)

    def init(self, runtime=0.5, lag_ratio=1):

        return ShowCreation(
            self.plane, run_time = runtime, lag_ratio = 1
        )

    def loop(self, loops, unit_time=1):

        for p in range(loops):
            lo = exp(-9.5-p)
            self.run(lag_order=lo, time_unit=unit_time)
            #if p == 0:
            #    self.play(FadeOut(title))

class Symmetric(ForwardDecomp):
    CONFIG = {
        "transposed_matrix": array([[2**-0.5, 1/pi], [1/pi, 2**-0.5]])
    }
    def construct(self):

        ForwardDecomp.construct(self)

class AngleParamd(ForwardDecomp):
    CONFIG = {
        "angle": pi/4
    }
    def construct(self):
        self.transformed_matrix = array([
            [cos(self.angle), sin(self.angle)],
            [-sin(self.angle), cos(self.angle)]
        ])
        ForwardDecomp.construct(self)
       

class Diagonalizable1(ForwardDecomp):
    CONFIG = {
        "transposed_matrix": array([[2, 1/4], [4/3, 8/5]])
    }
    def construct(self):
        ForwardDecomp.construct(self)

class Diagonalizable2(ForwardDecomp):
    CONFIG = {
        "transpoed_matrix": array([[2,3], [1,4]])
    }
    def construct(self):
        ForwardDecomp.construct(self)



       
class TransformInfiniteGrid(LinearTransformationScene):
    ''' Currently keeping this because we want to reference text handling'''
    CONFIG = {
        "include_background_plane" : True,
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_WIDTH,
            "y_radius" : FRAME_HEIGHT,
        },
        "show_basis_vectors" : True
    }
    def construct(self):
        self.setup()

        title = TextMobject("decomposition of a symmetric matrix")

        self.play(Write(title))

        init = ShowCreation(
            self.plane, run_time = 0.5, lag_ratio = 1
        )

        defective = array([[2, 0.5], [1, 2.5]])

        diagonalizable = array([[2, 1/4], [4/3, 8/5]])

        diagonalizable2 = array([[2,3], [1,4]])

        symmetric = pi * array([[1/pi, 2**-0.5], [2**-0.5, 1/pi]])
       
        def isomorphism(A):
            eigenvalues, eigenvectors = eig(A)
            P = eigenvectors
            Lambda = diag(eigenvalues)
            P_inv = inv(eigenvectors)
            return P, Lambda, P_inv

        def run(A, time_unit=1, lag_order=10**-4):
            self.play(init)
            self.wait(exp(-2))

            P, Lambda, P_inv = isomorphism(A)

            self.apply_transposed_matrix(P, run_time=time_unit, lag_ratio=lag_order)
            self.apply_transposed_matrix(Lambda, run_time=time_unit, lag_ratio=lag_order)
            self.apply_transposed_matrix(P_inv, run_time=time_unit, lag_ratio=lag_order)

            self.apply_transposed_matrix(inv(A), run_time=time_unit*3, lag_ratio=lag_order)

            self.remove(init)

        self.play(ApplyMethod(title.shift,3*UP))

        for p in range(4):
            lo = exp(-9.5-p)
            run(defective, lag_order=lo)
            if p == 0:
                self.play(FadeOut(title))
