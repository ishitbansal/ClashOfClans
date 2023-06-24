import unittest
import king
import points as pt
import village


# Test Cases for UP direction
class TestMoveUp(unittest.TestCase):

    def setUp(self):
        self.King = king.getHero(0)
        self.V = village.createVillage(1)

    # check if King moves when dead
    def test_alive(self):
        self.King.position = [17, 35]
        old_pos = [17, 35]
        self.King.alive = False
        self.King.move('up', self.V)
        self.assertEqual(old_pos, self.King.position,
                         'King moving even after being dead')

    # check if King faces up
    def test_movement_facing(self):
        self.King.position = [17, 35]
        self.King.move('up', self.V)
        self.assertEqual(self.King.facing, 'up',
                         'King is facing at incorrect direction')

    # check movement at spawn point
    def test_movement_spawn(self):
        self.King.position = [1, 0]
        self.King.move('up', self.V)
        expected_pos = [0, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check movement at blank
    def test_movement_blank(self):
        self.King.position = [17, 35]
        self.King.move('up', self.V)
        expected_pos = [16, 35]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over townhall
    def test_movement_townhall(self):
        self.King.position = [10, 16]
        self.King.move('up', self.V)
        expected_pos = [10, 16]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wall
    def test_movement_wall(self):
        self.King.position = [4, 16]
        self.King.move('up', self.V)
        expected_pos = [4, 16]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over hut
    def test_movement_hut(self):
        self.King.position = [8, 12]
        self.King.move('up', self.V)
        expected_pos = [8, 12]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over cannon
    def test_movement_cannon(self):
        self.King.position = [14, 14]
        self.King.move('up', self.V)
        expected_pos = [14, 14]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wizardtower
    def test_movement_wizardtower(self):
        self.King.position = [8, 27]
        self.King.move('up', self.V)
        expected_pos = [8, 27]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves up
    def test_movement_general(self):
        self.King.position = [12, 17]
        self.King.move('up', self.V)
        expected_pos = [11, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King does not move out of bound
    def test_movement_outofbound(self):
        self.King.position = [0, 17]
        self.King.move('up', self.V)
        expected_pos = [0, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves
    def test_movement_speed(self):
        self.King.position = [17, 0]
        self.King.speed = 4
        self.King.move('up', self.V)
        expected_pos = [13, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves over a building
    def test_movement_speed_stop(self):
        self.King.position = [12, 17]
        self.King.speed = 8
        self.King.move('up', self.V)
        expected_pos = [10, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if HERO_POS is getting modified after moving up
    def test_movement_heropos(self):
        self.King.position = [12, 17]
        self.King.move('up', self.V)
        expected_pos = [11, 17]
        self.assertEqual(expected_pos, pt.HERO_POS,
                         'HERO_POS not getting updated after movement of King')

    # check if King's other attributes are same
    def test_movement_attributes(self):
        King_ = king.getHero(0)
        self.King.position = [12, 17]
        self.King.move('up', self.V)
        self.assertEqual(King_.speed, self.King.speed)
        self.assertEqual(King_.health, self.King.health)
        self.assertEqual(King_.max_health, self.King.max_health)
        self.assertEqual(King_.attack, self.King.attack)
        self.assertEqual(King_.AoE, self.King.AoE)
        self.assertEqual(King_.attack_radius, self.King.attack_radius)
        self.assertEqual(King_.alive, self.King.alive)


# Test Cases for DOWN direction
class TestMoveDown(unittest.TestCase):

    def setUp(self):
        self.King = king.getHero(0)
        self.V = village.createVillage(1)

    # check if King moves when dead
    def test_alive(self):
        self.King.position = [0, 0]
        old_pos = [0, 0]
        self.King.alive = False
        self.King.move('down', self.V)
        self.assertEqual(old_pos, self.King.position,
                         'King moving even after being dead')

    # check if King faces down
    def test_movement_facing(self):
        self.King.position = [17, 35]
        self.King.move('down', self.V)
        self.assertEqual(self.King.facing, 'down',
                         'King is facing at incorrect direction')

    # check movement at spawn point
    def test_movement_spawn(self):
        self.King.position = [16, 0]
        self.King.move('down', self.V)
        expected_pos = [17, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check movement at blank
    def test_movement_blank(self):
        self.King.position = [0, 0]
        self.King.move('down', self.V)
        expected_pos = [1, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over townhall
    def test_movement_townhall(self):
        self.King.position = [5, 16]
        self.King.move('down', self.V)
        expected_pos = [5, 16]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wall
    def test_movement_wall(self):
        self.King.position = [2, 16]
        self.King.move('down', self.V)
        expected_pos = [2, 16]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over hut
    def test_movement_hut(self):
        self.King.position = [5, 12]
        self.King.move('down', self.V)
        expected_pos = [5, 12]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over cannon
    def test_movement_cannon(self):
        self.King.position = [11, 14]
        self.King.move('down', self.V)
        expected_pos = [11, 14]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wizardtower
    def test_movement_wizardtower(self):
        self.King.position = [6, 27]
        self.King.move('down', self.V)
        expected_pos = [6, 27]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves down
    def test_movement_general(self):
        self.King.position = [12, 17]
        self.King.move('down', self.V)
        expected_pos = [13, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King does not move out of bound
    def test_movement_outofbound(self):
        self.King.position = [17, 17]
        self.King.move('down', self.V)
        expected_pos = [17, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves
    def test_movement_speed(self):
        self.King.position = [0, 0]
        self.King.speed = 4
        self.King.move('down', self.V)
        expected_pos = [4, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves over a building
    def test_movement_speed_stop(self):
        self.King.position = [12, 17]
        self.King.speed = 8
        self.King.move('down', self.V)
        expected_pos = [14, 17]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if HERO_POS is getting modified after moving down
    def test_movement_heropos(self):
        self.King.position = [12, 17]
        self.King.move('down', self.V)
        expected_pos = [13, 17]
        self.assertEqual(expected_pos, pt.HERO_POS,
                         'HERO_POS not getting updated after movement of King')

    # check if King's other attributes are same
    def test_movement_attributes(self):
        King_ = king.getHero(0)
        self.King.position = [12, 17]
        self.King.move('down', self.V)
        self.assertEqual(King_.speed, self.King.speed)
        self.assertEqual(King_.health, self.King.health)
        self.assertEqual(King_.max_health, self.King.max_health)
        self.assertEqual(King_.attack, self.King.attack)
        self.assertEqual(King_.AoE, self.King.AoE)
        self.assertEqual(King_.attack_radius, self.King.attack_radius)
        self.assertEqual(King_.alive, self.King.alive)


# Test Cases for LEFT direction
class TestMoveLeft(unittest.TestCase):

    def setUp(self):
        self.King = king.getHero(0)
        self.V = village.createVillage(1)

    # check if King moves when dead
    def test_alive(self):
        self.King.position = [0, 0]
        old_pos = [0, 0]
        self.King.alive = False
        self.King.move('left', self.V)
        self.assertEqual(old_pos, self.King.position,
                         'King moving even after being dead')

    # check if King faces left
    def test_movement_facing(self):
        self.King.position = [17, 35]
        self.King.move('left', self.V)
        self.assertEqual(self.King.facing, 'left',
                         'King is facing at incorrect direction')

    # check movement at spawn point
    def test_movement_spawn(self):
        self.King.position = [17, 1]
        self.King.move('left', self.V)
        expected_pos = [17, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check movement at blank
    def test_movement_blank(self):
        self.King.position = [0, 35]
        self.King.move('left', self.V)
        expected_pos = [0, 34]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over townhall
    def test_movement_townhall(self):
        self.King.position = [13, 15]
        self.King.move('left', self.V)
        expected_pos = [13, 15]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wall
    def test_movement_wall(self):
        self.King.position = [4, 10]
        self.King.move('left', self.V)
        expected_pos = [4, 10]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over hut
    def test_movement_hut(self):
        self.King.position = [7, 13]
        self.King.move('left', self.V)
        expected_pos = [7, 13]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over cannon
    def test_movement_cannon(self):
        self.King.position = [12, 15]
        self.King.move('left', self.V)
        expected_pos = [12, 15]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wizardtower
    def test_movement_wizardtower(self):
        self.King.position = [17, 28]
        self.King.move('left', self.V)
        expected_pos = [17, 28]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves left
    def test_movement_general(self):
        self.King.position = [12, 17]
        self.King.move('left', self.V)
        expected_pos = [12, 16]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King does not move out of bound
    def test_movement_outofbound(self):
        self.King.position = [9, 0]
        self.King.move('left', self.V)
        expected_pos = [9, 0]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves
    def test_movement_speed(self):
        self.King.position = [0, 35]
        self.King.speed = 4
        self.King.move('left', self.V)
        expected_pos = [0, 31]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves over a building
    def test_movement_speed_stop(self):
        self.King.position = [12, 17]
        self.King.speed = 8
        self.King.move('left', self.V)
        expected_pos = [12, 15]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if HERO_POS is getting modified after moving left
    def test_movement_heropos(self):
        self.King.position = [12, 17]
        self.King.move('left', self.V)
        expected_pos = [12, 16]
        self.assertEqual(expected_pos, pt.HERO_POS,
                         'HERO_POS not getting updated after movement of King')

    # check if King's other attributes are same
    def test_movement_attributes(self):
        King_ = king.getHero(0)
        self.King.position = [12, 17]
        self.King.move('left', self.V)
        self.assertEqual(King_.speed, self.King.speed)
        self.assertEqual(King_.health, self.King.health)
        self.assertEqual(King_.max_health, self.King.max_health)
        self.assertEqual(King_.attack, self.King.attack)
        self.assertEqual(King_.AoE, self.King.AoE)
        self.assertEqual(King_.attack_radius, self.King.attack_radius)
        self.assertEqual(King_.alive, self.King.alive)


# Test Cases for RIGHT direction
class TestMoveRight(unittest.TestCase):

    def setUp(self):
        self.King = king.getHero(0)
        self.V = village.createVillage(1)

    # check if King moves when dead
    def test_alive(self):
        self.King.position = [17, 35]
        old_pos = [17, 35]
        self.King.alive = False
        self.King.move('right', self.V)
        self.assertEqual(old_pos, self.King.position,
                         'King moving even after being dead')

    # check if King faces right
    def test_movement_facing(self):
        self.King.position = [17, 35]
        self.King.move('right', self.V)
        self.assertEqual(self.King.facing, 'right',
                         'King is facing at incorrect direction')

    # check movement at spawn point
    def test_movement_spawn(self):
        self.King.position = [0, 34]
        self.King.move('right', self.V)
        expected_pos = [0, 35]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check movement at blank
    def test_movement_blank(self):
        self.King.position = [17, 0]
        self.King.move('right', self.V)
        expected_pos = [17, 1]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over townhall
    def test_movement_townhall(self):
        self.King.position = [9, 15]
        self.King.move('right', self.V)
        expected_pos = [9, 15]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wall
    def test_movement_wall(self):
        self.King.position = [4, 25]
        self.King.move('right', self.V)
        expected_pos = [4, 25]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over hut
    def test_movement_hut(self):
        self.King.position = [7, 10]
        self.King.move('right', self.V)
        expected_pos = [7, 10]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over cannon
    def test_movement_cannon(self):
        self.King.position = [12, 12]
        self.King.move('right', self.V)
        expected_pos = [12, 12]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves over wizardtower
    def test_movement_wizardtower(self):
        self.King.position = [17, 26]
        self.King.move('right', self.V)
        expected_pos = [17, 26]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King moves right
    def test_movement_general(self):
        self.King.position = [12, 17]
        self.King.move('right', self.V)
        expected_pos = [12, 18]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King does not move out of bound
    def test_movement_outofbound(self):
        self.King.position = [9, 35]
        self.King.move('right', self.V)
        expected_pos = [9, 35]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if King with high speed moves
    def test_movement_speed(self):
        self.King.position = [0, 0]
        self.King.speed = 4
        self.King.move('right', self.V)
        expected_pos = [0, 4]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

   # check if King with high speed moves over a building
    def test_movement_speed_stop(self):
        self.King.position = [11, 17]
        self.King.speed = 8
        self.King.move('right', self.V)
        expected_pos = [11, 21]
        self.assertEqual(self.King.position, expected_pos,
                         'Incorrect position of King')

    # check if HERO_POS is getting modified after moving right
    def test_movement_heropos(self):
        self.King.position = [12, 17]
        self.King.move('right', self.V)
        expected_pos = [12, 18]
        self.assertEqual(expected_pos, pt.HERO_POS,
                         'HERO_POS not getting updated after movement of King')

    # check if King's other attributes are same
    def test_movement_attributes(self):
        King_ = king.getHero(0)
        self.King.position = [12, 17]
        self.King.move('right', self.V)
        self.assertEqual(King_.speed, self.King.speed)
        self.assertEqual(King_.health, self.King.health)
        self.assertEqual(King_.max_health, self.King.max_health)
        self.assertEqual(King_.attack, self.King.attack)
        self.assertEqual(King_.AoE, self.King.AoE)
        self.assertEqual(King_.attack_radius, self.King.attack_radius)
        self.assertEqual(King_.alive, self.King.alive)


loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(TestMoveUp)
suite.addTests(loader.loadTestsFromTestCase(TestMoveDown))
suite.addTests(loader.loadTestsFromTestCase(TestMoveLeft))
suite.addTests(loader.loadTestsFromTestCase(TestMoveRight))
result = unittest.TextTestRunner().run(suite)

if (result.wasSuccessful()):
    with open("output.txt", "w") as f:
        f.write('True')
    print(True)
else:
    with open("output.txt", "w") as f:
        f.write('False')
    print(False)
