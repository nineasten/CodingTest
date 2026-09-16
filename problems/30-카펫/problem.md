# 문제

**출처**: 프로그래머스 · 코딩테스트 고득점 Kit · 완전탐색  
**문제 ID**: 42842  
**링크**: https://school.programmers.co.kr/learn/courses/30/lessons/42842  
**난이도**: Lv.2  
**카테고리**: 완전탐색

## 요약

Leo가 카펫을 구입하려고 한다. 카펫 사진이 흐릿해서 갈색(brown)과 노란색(yellow) 격자 개수만 보인다.

카펫의 구조:
- 앞쪽(테두리)은 갈색(brown)
- 뒤쪽(내부)은 노란색(yellow)
- 가로 길이 ≥ 세로 길이

brown과 yellow 개수가 주어질 때, 카펫의 **세로 길이, 가로 길이**를 구하시오.

## 제약

- `1 ≤ brown ≤ 5,120`
- `1 ≤ yellow ≤ 2,000,000`
- brown + yellow ≤ 10,000,000

## 입출력 예

| brown | yellow | result |
|---|---|---|
| 10 | 2 | [4, 3] |
| 8 | 1 | [3, 3] |
| 24 | 24 | [8, 6] |

### 설명

**예 1**: brown=10, yellow=2
```
BBBBBB
BYYB
BBBBBB
```
세로 3, 가로 4 → [4, 3]

## 목표

**시간 복잡도**: O(√yellow) ≈ O(1,414)  
**공간 복잡도**: O(1)

**풀이 아이디어**:  
1. 전체 격자 = brown + yellow
2. brown = 테두리 = height × width - (height-2) × (width-2)
3. 따라서 (height-2) × (width-2) = yellow
4. yellow의 약수 쌍 (a, b)를 찾아 height = a+2, width = b+2
5. width ≥ height 조건으로 역순 배치
