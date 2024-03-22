import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeSort {
    public static List<Integer> combineSortedLists(List<Integer> left, List<Integer> right) {
        List<Integer> results = new ArrayList<>();
        int i = 0;
        int j = 0;
        while (i < left.size() && j < right.size()) {
            if (left.get(i) < right.get(j)) {
                results.add(left.get(i++));
            } else {
                results.add(right.get(j++));
            }
        }
        results.addAll(left.subList(i, left.size()));
        results.addAll(right.subList(j, right.size()));
        return results;
    }

    public static List<Integer> mergeSort(List<Integer> list) {
        if (list.size() < 2) {
            return list;
        }
        int middle = list.size() / 2;
        List<Integer> left = mergeSort(list.subList(0, middle));
        List<Integer> right = mergeSort(list.subList(middle, list.size()));
        return combineSortedLists(left, right);
    }

    public static void main(String[] args) {
        try {
            List<Integer> a = Arrays.stream(args).map(Integer::parseInt).toList();
            System.out.println(mergeSort(a));
        } catch (NumberFormatException e) {
            System.out.println("stop it");
        }
    }
}
