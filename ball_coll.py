def ball_collide(x1,y1,r1,x2,y2,r2):
    dist=((x2-x1)**2+(y2-y1)**2)**0.5
    center=dist/2
    print("Collision Point",center)
    r=r1+r2
    print("Sum of radius",r)
    if(center<=r):
        print("Balls are Colliding")
        return True
    else:
        print("Balls are not Colliding")
        return False    
 
c=ball_collide(4,4,3,2,2,3)
print(c)
c=ball_collide(100,200,20,200,100,10)
print(c)
