
import pydart2 as pydart

if __name__ == '__main__':
    print('Hello, PyDART!')

    pydart.init()
    print('pydart initialization OK')

    world = pydart.World(0.0005, './data/skel/cubes.skel')
    # world = pydart.World(0.0005)
    print('pydart create_world OK')
    # skel = world.add_skeleton('./data/skel/cubes.skel')
    print ('Skel added')
    while world.t < 2.0:
        if world.nframes % 100 == 0:
            skel = world.skeletons[-1]
            print("%.4fs: The last cube COM = %s" % (world.t, str(skel.C)))
        world.step()
