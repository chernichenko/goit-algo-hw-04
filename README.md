# Оцінка ефективності алгоритмів сортування

## Огляд

Ця програма реалізує три алгоритми сортування: Merge Sort, Insertion Sort та вбудований Timsort (функція `sorted()` в Python). Було проведено тестування їх продуктивності для різних розмірів вхідних даних. Тестування проводилося з масивами довжиною 100, 1000, 5000 та 10000 елементів. 

## Алгоритми

1. **Merge Sort**:
   - Часова складність: O(n log n)
   - Алгоритм розбиває масив на дві частини, сортує кожну рекурсивно і зливає відсортовані частини.
   
2. **Insertion Sort**:
   - Часова складність: O(n^2)
   - Підходить для малих масивів, оскільки з кожним елементом масив поступово упорядковується.
   
3. **Timsort**:
   - Часова складність: O(n log n)
   - Використовується за замовчуванням в Python для сортування. Поєднує Merge Sort і Insertion Sort для ефективної роботи з реальними даними.

## Висновки

1. **Merge Sort** продемонстрував стабільну продуктивність і значно випереджає Insertion Sort для великих масивів. Це підтверджується його складністю O(n log n), що робить його ефективним для сортування великих наборів даних.
   
2. **Insertion Sort** ефективний лише для малих масивів. З ростом кількості елементів його продуктивність різко знижується через квадратичну складність O(n^2).

3. **Timsort** (вбудоване сортування Python) показує найкращі результати для всіх розмірів масивів. Це пов'язано з його адаптивністю до реальних даних та оптимізованою комбінацією алгоритмів.

## Висновки щодо сортування кількох списків

Алгоритм `merge_k_lists` сортує кілька списків за допомогою Merge Sort. Він ефективно об'єднує та сортує елементи зі складністю O(n log n), де n – загальна кількість елементів у всіх списках.

---

**Рекомендація**: Для великих масивів або списків, що об'єднуються, слід використовувати Merge Sort або Timsort для досягнення кращої продуктивності. Для невеликих масивів можна використовувати Insertion Sort, хоча його продуктивність значно гірша при зростанні розміру масиву.
