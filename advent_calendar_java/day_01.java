import java.io.*
import java.nio.file.*
import java.util.*
import java.util.stream.*

public class AdventOfCode2024 {

    // Method to extract data from the CSV file and return it as a List of DataEntry
    public static List < DataEntry > extract(String path) throws IOException {
        List < String > lines = Files.readAllLines(Paths.get(path));
        List < DataEntry > data = new ArrayList<>();

        for (String line: lines) {
            String[] parts = line.split("\\s{3}"); // Split by 3 spaces
            if (parts.length == 2) {
                int left = Integer.parseInt(parts[0].trim());
                int right = Integer.parseInt(parts[1].trim());
                data.add(new DataEntry(left, right));
            }
        }
        return data;
    }

    // Method to calculate the difference score
    public static int diffScore(List < DataEntry > data) {
        List < Integer > leftList = data.stream().map(entry -> entry.left).sorted().collect(Collectors.toList());
        List < Integer > rightList = data.stream().map(entry -> entry.right).sorted().collect(Collectors.toList());

        int diffSum = 0;
        for (int i=0; i < data.size(); i++) {
            diffSum += Math.abs(leftList.get(i) - rightList.get(i));
        }

        return diffSum;
    }

    // Method to calculate the similarity score
    public static int similarityScore(List < DataEntry > data) {
        Map < Integer, Long > rightCounts = data.stream()
        .collect(Collectors.groupingBy(entry -> entry.right, Collectors.counting()));

        int similaritySum = 0;
        for (DataEntry entry: data) {
            int similarity = entry.left * rightCounts.getOrDefault(entry.left, 0L).intValue();
            similaritySum += similarity;
        }

        return similaritySum;
    }

    // Main method to execute the program
    public static void main(String[] args) throws IOException {
        List < DataEntry > data = extract("data/day_01.csv");

        int diff = diffScore(data);
        int similarity = similarityScore(data);

        System.out.println(diff + " " + similarity);
    }

    // Helper class to represent each data entry with left and right values
    static class DataEntry {
        int left;
        int right;

        public DataEntry(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }
}
