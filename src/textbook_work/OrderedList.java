package textbook_work;

import java.util.Objects;
import java.util.Random;
import java.util.Arrays;
import java.util.stream.Collectors;

@SuppressWarnings("unchecked")
public class OrderedList<T extends Comparable<T>> {
    /**
     *
     */
    private final static int defaultInitialSize = 10;

    /**
     *
     */
    private Object[] internalArray;

    /**
     * The number of publicly visible objects.
     */
    private int numObjects;

    private String type;

    public OrderedList() {
        this(defaultInitialSize);
    }

    public OrderedList(int initialSize) {
        internalArray = new Object[initialSize];
    }

    public OrderedList(Object[] collection) {
        throw new UnsupportedOperationException("Not implemented yet");
    }

    public int size() {
        return numObjects;
    }

    private void grow() {
        int size = internalArray.length * 2;
        internalArray = Arrays.copyOf(internalArray, size);
    }

    /**
     * Binary search
     *
     * @param objToFind thing to look for
     * @return an index that is either the objects, or an insertion point
     */
    private int find_insertion_point(T objToFind) {
        int left = 0;
        int right = numObjects - 1;
        int mid = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            Object o = 2;
            switch (Integer.signum(objToFind.compareTo((T) internalArray[mid]))) {
                case 0:
                    return mid;
                case 1:
                    left = mid + 1;
                    break;
                case -1:
                    right = mid - 1;
                    break;
            }
        }
        return left;
    }

    /**
     * public find, properly returns non-index for "not in"
     *
     * @param objToFind
     * @return index if found, -1 if not
     */
    public int find_first(T objToFind) {
        int index = find_insertion_point(objToFind);
        if (objToFind.compareTo((T) internalArray[index]) == 0) {
            return index;
        } else {
            return -1;
        }
    }

    public int add(T objToAdd) {
        if (numObjects == internalArray.length) {
            grow();
        }
        int indexToAdd = find_insertion_point(objToAdd);
        for (int i = numObjects; i > indexToAdd; i--) {
            internalArray[i] = internalArray[i - 1];
        }
        internalArray[indexToAdd] = objToAdd;
        numObjects += 1;
        return numObjects;
    }

    public String toString() {
        return "OrderedList[" + Arrays.stream(internalArray).limit(numObjects).map(Objects::toString).collect(Collectors.joining(", ")) + "] (" + numObjects + ")";
    }


    public int deleteAll(T objToDelete) {

        return numObjects;
    }

    public int deleteAt(int index) {
        return numObjects;
    }

    public static void main(String[] args) {
        OrderedList<Integer> l = new OrderedList<Integer>();
        new Random().ints(10000,0,10).forEach(l::add);
        System.out.println(l);
    }
}
