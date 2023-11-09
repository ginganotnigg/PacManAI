- Course: Artificial Intelligence - HCMUS  
- Contributors:
  * [21120040 - Phạm Công Bằng](https://github.com/ginganotnigg)
  * [21120045 - Bùi Hồng Đăng](https://github.com/bhdang311003)
  * [21120182 - Phan Trí Nhân](https://github.com/TreeDude03)
  * [21120413 - Bùi Thiên Bảo](https://github.com/baobui1509)
  * [20120564 - Nguyễn Hoài Sơn](https://github.com/nguyenhoaisonHCMUS)

<h1 align='center'>PROJECT 1 - SEARCH (PACMAN)</h1>

## Problem Description
You are given a file that describes Pac-man World. Propose or apply learned algorithms to help Pac-Man find food without dying by monsters.

<p align='center'><img align='center' src="http://ai.berkeley.edu/images/pacman_game.gif"></p>

Pacman or monsters only moves in 4 direction (left, right, bottom, up) and cannot move over or through the wall. The game has four levels:
- Level 1: Pac-man knows the food’s position on the map and monsters do not appear in map. There is only one food on the map.
- Level 2: monsters stand in the place ever (never move around). If Pac-man pass through the monster or vice versa, game is over. There is still one food on the map and Pac-man knows its position.
- Level 3: Pac-man cannot see the foods if they are outside Pac-man’s nearest threestep. It means that Pac-man just only scans all the adjacent him (8 tiles x 3). There are many foods on the map. Monsters just move one step in any valid direction (if any) around the initial location at the start of the game. With each step Pac-man goes, each step Monsters move.
- Level 4 (difficult): map is opened. Monsters will seek and kill Pac-man. Pac-man wants to get food as much as possible. Pacman will die if at least one monster passes him. It is fine for monsters to go through each other. With each step Pacman goes, each step Monsters move. The food is so many. 

Game points are calculated as following rules:
- With each moving step, your point will be decreased by 1.
- For each food you take, 20 points will be given to you.

You may need to run your algorithm on many different graphs to make a comprehensive comparison of these algorithms’ performance regarding the following aspects:
- Time to finished
- The length of the discovered paths

In particular, you should generate some difficult maps such as Pac-man staying among two monsters or walls around all sides.
