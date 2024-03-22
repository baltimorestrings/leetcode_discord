import java.util.Arrays;

public class InsertionSort {
    public static void insertionSort(int[] l) {
        for (int i = 1; i < l.length; i++) {
            int j = i - 1;
            int val = l[i];
            if (val < l[j]) {
                while (j >= 0 && val < l[j]) {
                    l[j + 1] = l[j];
                    j--;
                }
                l[j + 1] = val;
            }
        }
    }

    public static void main(String[] args) {
        int[] a = new int[]{100, 4, 3, 1000, 1, 1, 1, 1};
        insertionSort(a);
        System.out.println(Arrays.toString(a));
    }
}
