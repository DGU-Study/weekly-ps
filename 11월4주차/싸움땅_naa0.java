import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Player {
    int num, x, y, d, s, a;

    public Player(int num, int x, int y, int d, int s, int a) {
        this.num = num;
        this.x = x;
        this.y = y;
        this.d = d;
        this.s = s;
        this.a = a; // 공격력
    }
}

class Tuple {
    int x, y, dir;

    public Tuple(int x, int y, int dir) {
        this.x = x;
        this.y = y;
        this.dir = dir;
    }
}

class Pair {
    int x, y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public boolean isSame(Pair p) {
        return this.x == p.x && this.y == p.y;
    }
}


public class Main {
    public static final Player EMPTY = new Player(-1, -1, -1, -1, -1, -1);
    public static final int DIR_NUM = 4;
    public static final int MAX_M = 30; //  m 최댓값
    public static final int MAX_N = 20; //  n 최댓값

    //  변수 선언
    public static int n, m, k;

    //  총 목록 관리 (정수 배열)
    public static ArrayList<Integer>[][] gun = new ArrayList[MAX_M][MAX_N];
    //  플레이어 목록 관리 (Player 객체 배열)
    public static Player[] players = new Player[MAX_M];

    //  dx, dy
    public static int[] dx = new int[]{-1, 0, 1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};

    //  플레이어들의 포인트 정보를 기록합니다.
    public static int[] points = new int[MAX_M];

    //  (x, y)가 격자를 벗어나는지 확인합니다.
    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    //  현재 (x, y) 위치에서 방향 d를 보고 있을 때
    //  그 다음 위치와 방향을 찾아줌
    public static Tuple getNext(int x, int y, int d) {
        int nx = x + dx[d], ny = y + dy[d];

        //  격자 벗어나면 방향을 반대방향으로 이동
        if(!inRange(nx, ny)){
            // 반대 방향 : 0 <-> 2 / 1 <-> 3
            d = (d < 2) ? (d + 2) : (d - 2);
            nx = x + dx[d]; ny = y + dy[d]; 
        }

        return new Tuple(nx, ny, d);
    }

    // 특정 칸에 있는 Player 반환
    public static Player findPlayer(Pair pos){
        for (int i=0; i<m; i++){
            int x = players[i].x, y = players[i].y;
            if(pos.isSame(new Pair(x, y)))
                return players[i];
        }
        return EMPTY;
    }

    public static void update(Player p){
        int num = p.num;

        for(int i = 0; i < m; i++){
            int numI = players[i].num;
            if(numI == num) {
                players[i] = p;
                break;
            }
        }
    }

    public static void move(Player p, Pair pos){
        int num = p.num, x = p.x, y = p.y, d = p.d, s = p.s, a = p.a;
        int nx = pos.x, ny = pos.y;

        gun[nx][ny].add(a);
        Collections.sort(gun[nx][ny]);
        a = gun[nx][ny].get(gun[nx][ny].size() - 1);
        gun[nx][ny].remove(gun[nx][ny].size() - 1);

        p = new Player(num, nx, ny, d, s, a);
        update(p);
    }

    public static void loserMove(Player p){
        int num = p.num, x = p.x, y = p.y, d = p.d, s = p.s, a = p.a;

        // 현재 위치에 총을 내려놓게 됨.
        gun[x][y].add(a);

        for(int i = 0; i <4; i++){
            int ndir = (d + i) % 4;
            int nx = x + dx[ndir], ny = y + dy[ndir];

            if(inRange(nx, ny) && findPlayer(new Pair(nx, ny)) == EMPTY){
                p = new Player(num, x, y, ndir, s, 0);
                move(p, new Pair(nx, ny));
                break;
            }
        }
    }

    // p2과 p2가 pos에서 
    public static void duel(Player p1, Player p2, Pair pos){
        int num1 = p1.num, d1 = p1.d, s1 = p1.s, a1 = p1.a;
        int num2 = p2.num, d2 = p2.d, s2 = p2.s, a2 = p2.a;

        // p1이 이긴 경우
        if(s1 + a1 > s2 + a2 || (s1 + a1 == s2 + a2 && s1 > s2)){
            // p2는 포인트 얻게 됨.
            points[num1] += (s1 + a1) - (s2 + a2);
            // p1은 진 사람의 움직임 진행
            loserMove(p2);
            // 이후 p2는 이긴 사람의 움직임을 진행함.
            move(p1, pos);
        }
        // p2는 포인트를 얻게 됨.
        else {
            // p2는 포인트를 얻게 됨.
            points[num2] += (s2 + a2) - (s1 + a1);
            // p1은 진 사람의 움직임을 진행.
            loserMove(p1);
            // 이후 p2는 이긴 사람의 움직임을 진행.
            move(p2, pos);
        }
    }


    public static void simulate() {
        // 첫 번째 플레이어부터 순서대로 진행
        for(int i = 0; i < m; i++){
            int num = players[i].num;
            int x = players[i].x;
            int y = players[i].y;
            int d = players[i].d;
            int s = players[i].s;
            int a = players[i].a;

            // 현재 플레이어가 움직일 그 다음 위치와 방향 구하기
            Tuple next = getNext(x, y, d);
            int nx = next.x, ny = next.y, ndir = next.dir;

            // 해당 위치에 있는 이전 플레이어 정보 받기
            Player nextPlayer = findPlayer(new Pair(nx, ny));

            // 현재 플레이어의 위치와 방향 보정
            Player currPlayer = new Player(num, nx, ny, ndir, s, a);
            update(currPlayer);

            // 해당 위치로 이동해서 플레이어가 없으면 그대로 움직임
            if(nextPlayer == EMPTY)
                move(currPlayer, new Pair(nx, ny));
            // 해당 위치에 플레이어가 있다면 결투 진행
            else
                duel(currPlayer, nextPlayer, new Pair(nx, ny));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //  입력
        n = sc.nextInt();   //  격자 크기
        m = sc.nextInt();   //  플레이어 수
        k = sc.nextInt();   // 라운드 수

        //  총 정보 입력
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                gun[i][j] = new ArrayList<>();

                int num = sc.nextInt();
                //  총이 놓여있는 칸 일 때만 입력
                if (num != 0)
                    gun[i][j].add(num);
            }
        }

        //  플레이어 정보 입력
        for(int i = 0; i < m; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            int d = sc.nextInt();
            int s = sc.nextInt();

            players[i] = new Player(i, x-1, y-1, d, s, 0);
        }

        while (k-- > 0)
            simulate();

        // 각 플레이어 획득 포인트 출력
        for (int i = 0; i < m; i++)
            System.out.print(points[i] + " ");
    }
}