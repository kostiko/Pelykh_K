class Ball(object):
    def __init__(self,sup='regular'):
        self.ball_type = sup

ball1 = Ball()
ball2 = Ball("super")
print (ball1.ball_type)
print (ball2.ball_type)