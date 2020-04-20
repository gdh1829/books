# Passing code with parameterization

## Behavior parameterization

- is a software development pattern that lets you handle freequent requirement changes.
In a nutshell, it means taking a block of code and making it available without executing it.
- is the ability for a method to take multiple different behaviors as parameters and use them internally to accomplish different behaviors.
- lets you make your code more adaptive to changing requirements and saves on engineering efforts in the future.
- Passing code is a way to give new behaviors as arguments to a method. But it's verbose prior to Java 8. Anonymous classes helped a bit before Java 8 to get rid of the verbosity associated with declaring multiple concrete classes for an interface that are needed only once.
- The java API contains many methods that can be parameterized with different behaviors, which include sorting, threads, and GUI handling.

## Examples

1. 인벤토리에 사과가 아래와 같이 들어있다.
```java
public class DemoApplication {
    public static void main(String[] args) {
        new DemoApplication();
    }

    public DemoApplication() {
        List<Apple> inventory = Arrays.asList(
            new Apple(COLOR.GREEN, 150),
            new Apple(COLOR.RED, 100),
            new Apple(COLOR.GREEN, 200)
        );
    }

    // Apple property enum
    public enum COLOR {
        GREEN, RED
    }

    // Apple Bean
    public class Apple {
        private COLOR color;
        private int weight;

        public Apple(COLOR color, int weight) {
            this.color = color;
            this.weight = weight;
        }

        public COLOR getColor() {
            return color;
        }

        public int getWeight() {
            return weight;
        }
    }
}
```

1. 인벤토리의 사과를 출력해줄 함수를 두 가지 패턴으로 아래와 같이 생성
    - 자바 내장형 함수형 인터페이스인 Consumer<T>
    - 커스텀 함수형 인터페이스 AppleFormatter

```java
public class DemoApplication {
    // Built in Consumer functional interface behavior parameterization
    private static void prettyPrintApple(List<Apple> apples, Consumer<Apple> formatter) {
        for (Apple apple : apples) {
            formatter.accept(apple);
        }
    }

    // Custom Functional interface behavior parameterization
    private static void prettyPrintApple(List<Apple> apples, AppleFormatter formatter) {
        for (Apple apple : apples) {
            String output = formatter.accept(apple);
            System.out.println(output);
        }
    }

    // Functional interface
    public interface AppleFormatter {
        String accept(Apple a);
    }
}

1. 다양한 방법으로 behavior parameterization 시험 해보기
    - 익명 함수
    - 커스텀 함수형 인터페이스(AppleFormatter) implementation
    - 람다 표현

```java
public class DemoApplication {
    // anonymous class
    prettyPrintApple(inventory, new AppleFormatter() {
        public String accept(Apple a) {
            String characteristic = a.getWeight() > 150 ? "heavy" : "light";
            return new StringBuilder("A ")
                .append(characteristic)
                .append(" ")
                .append(a.getColor().toString().toLowerCase())
                .append(" apple")
                .toString();
        }
    });

    // lambda expression
    prettyPrintApple(inventory, (Apple a) -> System.out.println(
        new StringBuilder("A ") 
        .append(a.getWeight() > 150 ? "heavy" : "light") 
        .append(" ") 
        .append(a.getColor().toString().toLowerCase())
        .append(" apple")
        .toString()
    ));

    // Functional interface implementations
    prettyPrintApple(inventory, new AppleSimpleFormatter());
    prettyPrintApple(inventory, (Apple a) -> System.out.println("An apple of " + a.getWeight() + "g"));

    // Functional interface implementation
    public class AppleFancyFormatter implements AppleFormatter {
        public String accept(Apple a) {
            String characteristic = a.getWeight() > 150 ? "heavy" : "light";
            return new StringBuilder("A ")
                .append(characteristic)
                .append(" ")
                .append(a.getColor().toString().toLowerCase())
                .append(" apple")
                .toString();
        }
    }

    // Functional interface implementation
    public class AppleSimpleFormatter implements AppleFormatter {
        public String accept(Apple a) {
            return "An apple of " + a.getWeight() + "g";
        }
    }
}
```
