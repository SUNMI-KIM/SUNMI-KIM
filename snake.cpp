#include <ncurses.h>
#include <time.h>
#include <string>
#include <iostream>
#include <vector>
#include <thread>
#include <random>
#include "./map/map.cpp"
using namespace std;

int WIDTH = sizeof(map[0]) / sizeof(map[0][0]); // 40
int HEIGHT = sizeof(map) / sizeof(map[0]);      // 30

class Gate
{
public:
    pair<int,int> gate1;
    pair<int,int> gate2;
    Gate();
    ~Gate();
    void appearGate();
    void disappearGate();
};
class Snake
{
public:
    Snake(int x, int y);
    int head_x, head_y;
    char ahead; // n, s, e, w 초기 설정은 west
    int snake_length = 3;
    vector <pair<int, int>> body;
    int item[2];
    int itemType[2] = {6, 7};
    bool gameContinue;
    
    void setSnake();
    void showSnake();
    void moveSnake(Gate& gate);
    void showMap();
    void throughGate(Gate& gate);
    void SpawnItem();
    void DelItem();
    bool UnableItem(int p1, int p2);
    bool GetItem(int f, int s);
};
Snake::Snake(int x=20, int y=15)
{
    head_x = x;
    head_y = y;
    ahead = 'w';
    gameContinue = true;
}
void Snake::setSnake()
{
    body.push_back(pair<int,int>(head_y,head_x));
    body.push_back(pair<int, int>(head_y, head_x+1));
    body.push_back(pair<int, int>(head_y, head_x+2));
}
void Snake::showSnake()
{
    for(int i = 0; i < body.size(); i++)
        map[body[i].first][body[i].second] = 3;
}
void Snake::SpawnItem() {
    srand(time(NULL));
    int itemShape = rand() % 2;
    item[0] = rand() % 30;
    item[1] = rand() % 40;
    while (!UnableItem(item[0], item[1])) {
        item[0] = rand() % 30;
        item[1] = rand() % 40;
    }
    map[item[0]][item[1]] = itemType[itemShape];
}
void Snake::DelItem()
{
    map[item[0]][item[1]] = 0;
    SpawnItem();
}
bool Snake::UnableItem(int p1, int p2) {
    if (map[p1][p2] != 0) {
        return false;
    }
    return true;
}
bool Snake::GetItem(int f, int s)
{
    if(f = item[0] && s = item[1]) return true;
    return false;
}
bool Snake::diffItem(int f, int s){
    if(map[f][s] == itemType[0]){
        return true;
    }
    else if(map[f][s] == itemType[1]){
        return false;
    }
}
void Snake::moveSnake(Gate& gate)
{
    if (map[body[0].first][body[0].second]==5)
        throughGate(gate);
    else if (map[body[0].first][body[0].second]==1)
        gameContinue = false; 
    else body.insert(body.begin(), pair<int,int>(head_y,head_x));
    map[body.back().first][body.back().second] = 0;
    body.pop_back();     
    showSnake();  
}
void Snake::throughGate(Gate& gate)
{
    switch(ahead){
        case 'n': // 위로 진출
            if(head_y==gate.gate1.second && head_x==gate.gate1.first){
                body.insert(body.begin(), pair<int,int>(gate.gate2.second, gate.gate2.first));
                head_y = gate.gate2.second;
                head_x = gate.gate2.first;
                if(gate.gate2.second==0)
                    ahead = 'e';
                else if(gate.gate2.second==WIDTH-1)
                    ahead = 'w';
                else if(gate.gate2.first==0)
                    ahead = 's';
                else
                    ahead = 'n';
            }
            else{
                body.insert(body.begin(), pair<int,int>(gate.gate1.second, gate.gate1.first));
                head_y = gate.gate1.second;
                head_x = gate.gate1.first;
                if(gate.gate1.second==0)
                    ahead = 'e';
                else if(gate.gate1.second==WIDTH-1)
                    ahead = 'w';
                else if(gate.gate1.first==0)
                    ahead = 's';
                else
                    ahead = 'n';
            }
            break;
        case 's':
            break;
        case 'e':
            break;
        case 'w':
            break;    
    }
}
void Snake::showMap()
{

}


Gate::Gate()
{
    gate1 = pair<int,int>(0,0);
    gate2 = pair<int,int>(0,0);
}
Gate::~Gate()
{
}

void Gate::appearGate()
{
    do{    
        random_device rd1;
        mt19937 gen1(rd1());
        uniform_int_distribution<int> dis1(1, WIDTH-2);
        random_device rd2;
        mt19937 gen2(rd2());
        uniform_int_distribution<int> dis2(1, HEIGHT-2);
        int random = dis1(gen1);
        int random2 = dis2(gen2);
        if(random%4==0){
            gate1.first = random;
            gate1.second = 0;
        }
        else if(random%4==1){
            gate1.first = random;
            gate1.second = HEIGHT-1;
        }
        else if(random%4==2){
            gate1.first = 0;
            gate1.second = random2;
        }
        else{
            gate1.first = WIDTH-1;
            gate1.second = random2;
        }
        random = dis1(gen1);
        if(random%4==0){
            gate2.first = random;
            gate2.second = 0;
        }
        else if(random%4==1){
            gate2.first = random;
            gate2.second = HEIGHT-1;
        }
        else if(random%4==2){
            gate2.first = 0;
            gate2.second = random2;
        }
        else{
            gate2.first = WIDTH-1;
            gate2.second = random2;
        }
    }while(gate1.first==gate2.first && gate1.second==gate2.second);

    map[gate1.second][gate1.first] = 5;
    map[gate2.second][gate2.first] = 5;    
}
void Gate::disappearGate()
{
    map[gate1.second][gate1.first] = 1;
    map[gate2.second][gate2.first] = 1;
}

void color()
{
    start_color();
    init_pair(1, COLOR_WHITE, COLOR_WHITE);
    init_pair(2, COLOR_BLACK, COLOR_BLACK);
    init_pair(3, COLOR_WHITE, COLOR_RED);
    init_pair(4, COLOR_WHITE, COLOR_BLUE);
    init_pair(5, COLOR_GREEN, COLOR_GREEN);
    init_pair(6, COLOR_RED, COLOR_RED);
}
int main()
{
    initscr();
    color();
    resize_term(35, 80);
    border('@', '@', '@', '@', '@', '@', '@', '@');
    refresh();

    Snake MainSnake = Snake();
    Gate gate = Gate();

    WINDOW* gameBoard1 = newwin(30, 40, 2, 2);
    start_color();
    init_pair(1, COLOR_GREEN, COLOR_BLACK);
    attron(COLOR_PAIR(1));
    attroff(COLOR_PAIR(1));
    refresh();
    keypad(gameBoard1, TRUE);

    WINDOW* scoreBoard1 = newwin(14, 36, 3, 43);
    init_pair(3, COLOR_BLACK, COLOR_WHITE);
    wmove(scoreBoard1, 0, 0);
    wattron(scoreBoard1, COLOR_PAIR(3));
    wborder(scoreBoard1, '|', '|', '-', '-', '*', '*', '*', '*');
    wbkgd(scoreBoard1, COLOR_PAIR(3));
    mvwprintw(scoreBoard1, 3, 3, "body: %d", MainSnake.snake_length);
    mvwprintw(scoreBoard1, 4, 3, "grow: %d", MainSnake.snake_length);
    mvwprintw(scoreBoard1, 5, 3, "poison: %d", MainSnake.snake_length);
    mvwprintw(scoreBoard1, 6, 3, "gate: %d", MainSnake.snake_length);
    wrefresh(scoreBoard1);

    WINDOW* missionBoard1 = newwin(14, 36, 18, 43);
    MainSnake.setSnake();
    wbkgd(missionBoard1, COLOR_PAIR(6));
    init_pair(3, COLOR_BLACK, COLOR_WHITE);
    wmove(missionBoard1, 0, 0);
    wattron(missionBoard1, COLOR_PAIR(3));
    wborder(missionBoard1, '|', '|', '-', '-', '*', '*', '*', '*');
    wbkgd(missionBoard1, COLOR_PAIR(3));
    mvwprintw(missionBoard1, 3, 3, "body: %d", MainSnake.snake_length);
    mvwprintw(missionBoard1, 4, 3, "grow: %d", MainSnake.snake_length);
    mvwprintw(missionBoard1, 5, 3, "poison: %d", MainSnake.snake_length);
    mvwprintw(missionBoard1, 6, 3, "gate: %d", MainSnake.snake_length);
    wrefresh(missionBoard1);
    MainSnake.SpawnItem();
    int count = 0;
    while (MainSnake.gameContinue) {
        int key;
        noecho();
        key = wgetch(gameBoard1);

        if(count++%10==0){
            MainSnake.showSnake();
            
            gate.appearGate();
        }
        switch(key){
        case(KEY_DOWN):
            if(MainSnake.ahead!='n') {
                MainSnake.head_y += 1;
                MainSnake.ahead = 's';
                MainSnake.moveSnake(gate);
                if(MainSnake.GetItem(MainSnake.head_y, MainSnake.head_x){
                    if(MainSnake.diffItem(MainSnake.head_y, MainSnake.head_x)){
                        MainSnake.body.insert(MainSnake.body.begin(),(make_pair(MainSnake.body[0].first + 1, MainSnake.body[0].second)));
                    }
                    else{
                        MainSnake.body[0].first += 1;
                        map[MainSnake.back().first][MainSnake.back().second] = 0;
                        MainSnake.body.pop_back();
                    }
                }
            }
            break;
        case(KEY_UP):
            if(MainSnake.ahead!='s'){
                MainSnake.head_y -= 1;
                MainSnake.ahead = 'n';
                MainSnake.moveSnake(gate);
                if(MainSnake.GetItem(MainSnake.head_y, MainSnake.head_x){
                    if(MainSnake.diffItem(MainSnake.head_y, MainSnake.head_x)){
                        MainSnake.body.insert(MainSnake.body.begin(),(make_pair(MainSnake.body[0].first - 1, MainSnake.body[0].second)));
                    }
                    else{
                        MainSnake.body[0].first -= 1;
                        map[MainSnake.back().first][MainSnake.back().second] = 0;
                        MainSnake.body.pop_back();
                    }
                }
            }
            break;
        case(KEY_LEFT):
            if(MainSnake.ahead!='e'){
                MainSnake.head_x -= 1;
                MainSnake.ahead = 'w';
                MainSnake.moveSnake(gate);
                if(MainSnake.GetItem(MainSnake.head_y, MainSnake.head_x){
                    if(MainSnake.diffItem(MainSnake.head_y, MainSnake.head_x)){
                        MainSnake.body.insert(MainSnake.body.begin(),(make_pair(MainSnake.body[0].first, MainSnake.body[0].second - 1)));
                    }
                    else{
                        MainSnake.body[0].second -= 1;
                        map[MainSnake.back().first][MainSnake.back().second] = 0;
                        MainSnake.body.pop_back();
                    }
                }
            }
            break;
        case(KEY_RIGHT):
            if(MainSnake.ahead!='w'){
                MainSnake.head_x += 1;
                MainSnake.ahead = 'e';
                MainSnake.moveSnake(gate);
                if(MainSnake.GetItem(MainSnake.head_y, MainSnake.head_x){
                    if(MainSnake.diffItem(MainSnake.head_y, MainSnake.head_x)){
                        MainSnake.body.insert(MainSnake.body.begin(),(make_pair(MainSnake.body[0].first, MainSnake.body[0].second + 1)));
                    }
                    else{
                        MainSnake.body[0].second += 1;
                        map[MainSnake.back().first][MainSnake.back().second] = 0;
                        MainSnake.body.pop_back();
                    }
                }
            }
            break;
        }
 
        for (int i = 0; i < 30; i++) {
            for (int j = 0; j < 40; j++) {
                switch (map[i][j]) {
                case 0:
                    mvwprintw(gameBoard1, i, j, " ");
                    break;
                case 1:
                    mvwprintw(gameBoard1, i, j, "#");
                    break;
                case 3:
                    mvwprintw(gameBoard1, i, j, "*");
                    break;
                case 4:
                    mvwprintw(gameBoard1, i, j, "@");
                    break;
                case 5:
                    mvwprintw(gameBoard1, i, j, "D");
                    break;
                case 6:
                    mvwprintw(gameBoard1, i, j, "?");
                    break;
                case 7:
                    mvwprintw(gameBoard1, i, j, "?");
                    break;
                }
            }
        }
        if(count%10==9){
            gate.disappearGate();
            MainSnake.DelItem();
        }
        
    
    }
    wrefresh(gameBoard1);
    endwin();
    return 0;
}
