public class Задание4 {
    public static void main(String[] args) {
        int n = 6;
        int m = -100;
        int[][] array;
        array = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                array[i][j] = (int) (Math.random() * -10);
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                System.out.print(array[i][j] + "\t");
            }
            System.out.println("");
        }
        for (int i = array; i >= 0; i--) {
            System.out.print(a[i][array - i] + " ");
        }
        System.out.println();
