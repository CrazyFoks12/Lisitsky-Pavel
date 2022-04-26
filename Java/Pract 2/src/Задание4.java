public class Задание4 {
    public static void main(String[] args) {
        int n = 6;
        int m = 100;
        int[][] array;
        array = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                array[i][j] = (int) ((Math.random()*20)-10);
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                System.out.print(array[i][j] + "\t");
            }
            System.out.println("");
        }
        for (int j = array.length; j == 0; j--) {
            for (int i = array.length; i == 0; i--) {
                if (array[j][i] < m) {m = array[j][i];}
            }
        }
        /*for (int k = n-1; k > 0; k--) {
            if (array[k][k-1] > m && array[k][k-1] < 0) {
                m = array[k][k-1];
            }
        }*/
        System.out.println("максимальное отрицательное число: " + m);
        System.out.println();
    }
}