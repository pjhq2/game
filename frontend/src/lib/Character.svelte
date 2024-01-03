<script>
  import Inventory from "./Inventory.svelte";
  import Weapon from "./Weapon.svelte";
  import Skill from "./Skill.svelte";
  // 스텟
  let STR = 6;
  let DEX = 6;
  let INT = 6;
  let CON = 6;
  let LUK = 6;
  let 추가STR = 79;
  let 추가DEX = 79;
  let 추가INT = 79;
  let 추가CON = 79;
  let 추가LUK = 79;
  let 최종STR = 79;
  let 최종DEX = 79;
  let 최종INT = 79;
  let 최종CON = 79;
  let 최종LUK = 79;
  // 정보
  // 장비
  // 스킬
  let 이름 = "만패";
  let 레벨 = 21;
  let 직업 = "초보자";
  let HP = 2105;
  let MP = 100;
  let 공격력 = 106;
  let 치명타 = 0.21;
  let 치명타증폭 = 1.32;
  let 명중 = 22;
  let 방어력 = 64;
  let 내성 = 0.0;
  let 회피 = 0.0;
  let 회복 = 0;
  let 속도 = 1000;
  let 추가HP = 1488;
  let 추가MP = 0;
  let 추가공격력 = 79;
  let 추가치명타 = 0.15;
  let 추가치명타증폭 = 0.79;
  let 추가명중 = 188;
  let 추가방어력 = 303;
  let 추가내성 = 0.0;
  let 추가회복 = 0.13;
  let 추가회피 = 0.13;
  let 추가속도 = 0;
  let 최종HP = 1488;
  let 최종MP = 0;
  let 최종공격력 = 79;
  let 최종치명타 = 0.15;
  let 최종치명타증폭 = 0.79;
  let 최종명중 = 188;
  let 최종방어력 = 303;
  let 최종내성 = 0.0;
  let 최종회복 = 0.13;
  let 최종회피 = 0.13;
  let 최종속도 = 0;
  let 스킬리스트 = [{ 이름: "강타", 레벨: 1 }];
  $: 임시 = 스킬리스트;
  let 경험치 = 500;
  let 필요경험치 = 3000;
  let 코인 = 198;
  let 인벤토리 = { 이름: "만패의 인벤토리" };
  let 무기 = { 이름: "혼령의 구슬", 레벨: 1 };
</script>

<div on:new={처음생성}>
  <div>====================</div>
  <div><span style="font-weight: 700">{이름}[{직업}]</span> Lv.{레벨}</div>
  <div>====================</div>
  <div><span style="color: red; font-weight: 700">혼령의 구슬</span>(+6)</div>
  <div style="padding: 0px 0px 0px 180px">무기</div>
  <div>등급 : 영웅</div>
  <div>INT : +16</div>
  <div>최소데미지 : 55(+0)</div>
  <div>최대데미지 : 70(+0)</div>
  <div>증폭 : 1.0(+0.00)</div>
  <div>무기데미지 : 55 - 70</div>
  <div>무기 스킬 : 매혹 Lv.1</div>
  <div style="padding: 0px 0px 0px 85px">요괴화 Lv.1</div>
  <div>----------------------------------</div>
  <div>HP : {HP}(+{추가HP})</div>
  <div>MP : {MP}(+{추가MP})</div>
  <div>STR : {STR}(+{추가STR})</div>
  <div>DEX : {DEX}(+{추가DEX})</div>
  <div>INT : {INT}(+{추가INT})</div>
  <div>CON : {CON}(+{추가CON})</div>
  <div>LUK : {LUK}(+{추가LUK})</div>
  <div>공격력 : {공격력}(+{추가공격력})</div>
  <div>방어력 : {방어력}(+{추가방어력})</div>
  <div>치명타 : {치명타}(+{추가치명타})</div>
  <div>치명타증폭 : {치명타증폭}(+{추가치명타증폭})</div>
  <div>명중 : {명중}(+{추가명중})</div>
  <div>회피 : {회피}(+{추가회피})</div>
  <div>최종데미지 : {최종공격력} - {최종공격력}</div>
  <div>
    보유스킬 :
    {#each 스킬리스트 as 스킬, i (스킬)}
      <span class="스킬">{스킬.이름} Lv.{스킬.레벨}</span>
    {/each}
  </div>
  <div>경험치 : {경험치} / {필요경험치}</div>
  <div>코인 : {코인}</div>
  <div>====================</div>
</div>

<style>
</style>
