import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input(){
        str = scan.next();
    }
    static void pro(){
        int min = Integer.MAX_VALUE;

        int aCnt = 0;
        for(char c: str.toCharArray()) {
            if(c =='a') {
                aCnt++;
            }
        }

        for(int i=0; i<str.length(); i++) {
            int bCnt = 0;
            for(int j=i; j<i+aCnt; j++) {
                int idx = j%str.length(); // 문자열이 원형이기 때문에 idx를 순환하도록 처리
                if(str.charAt(idx) =='b') {
                    bCnt++;
                }
            }
            min = Math.min(min, bCnt);
        }
        System.out.println(min);
    }

    static String str = "";

    public static void main(String[] args) {
        input();
        pro();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}