
public class Задание1 {
    public static void main(String[] args) {
        int [] intArray = new int [] {-1,2,3,4,5,6,7};
        int min = intArray[0];
        for (int num : intArray) {
	        if (num < min) {
	            min = num;
	        }
	    }
        System.out.println("Minimum in massive " + min);
       for(int i=0; i<intArray.length; i++) {
           System.out.println(intArray[i]*min);
       }
    }
}