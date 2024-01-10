import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:frontend/models/weapon_model.dart';
import 'package:frontend/models/skill_model.dart';

class WeaponWidget extends StatelessWidget {
  final WeaponModel weapon;

  WeaponWidget({required this.weapon});

  @override
  Widget build(BuildContext context) {
    var addiAbilityKeys = [];
    var addiAbilityValues = [];
    var weaponSkillListKeys = [];
    var weaponSkillListValues = [];
    weapon.addiAbility?.forEach((key, value) {
      addiAbilityKeys.add(key);
      addiAbilityValues.add(value);
    });
    for(int i=0; i<weapon.weaponSkillList.length; i++) {
      weapon.weaponSkillList[i].forEach((key, value) {
        weaponSkillListKeys.add(key);
        weaponSkillListValues.add(value);
      });
    }

    return Container(
      // padding: EdgeInsets.all(20),
      padding: EdgeInsets.fromLTRB(20, 20, 20, 20),
      decoration: BoxDecoration(
        color: Colors.black54,
        borderRadius: BorderRadius.circular(6),
        border: Border.all(
          color: Colors.black,
          width: 1,
        ),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Text('${weapon.name}(+${weapon.reinLevel})', style: TextStyle(color: Colors.yellowAccent, fontWeight: FontWeight.w700),),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              Text('${weapon.type}', style: TextStyle(color: Colors.white70))
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
            Flexible(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('등급', style: TextStyle(color: Colors.white70)),
                  Column(children: addiAbilityKeys.map((item) => Text(item, style: TextStyle(color: Colors.white70),)).toList()),
                  Text('최소데미지', style: TextStyle(color: Colors.white70)),
                  Text('최대데미지', style: TextStyle(color: Colors.white70)),
                  Text('무기데미지', style: TextStyle(color: Colors.white70)),
                  Text('무기스킬', style: TextStyle(color: Colors.white70)),
              ],
            ), flex: 4,),
            Flexible(
              child: Container(),
              flex: 2,),
            Flexible(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('${weapon.gradeName}', style: TextStyle(color: Colors.white70)),
                  Column(children: addiAbilityValues.map((item) => Text('+${item}', style: TextStyle(color: Colors.white70),)).toList()),
                  Text('${weapon.minDamage}(+${weapon.reinMinDamage})', style: TextStyle(color: Colors.white70)),
                  Text('${weapon.maxDamage}(+${weapon.reinMaxDamage})', style: TextStyle(color: Colors.white70)),
                  Text('${weapon.finalMinDamage} - ${weapon.finalMaxDamage}', style: TextStyle(color: Colors.white70)),
                  Text('${weaponSkillListValues[0]} Lv.${weaponSkillListValues[1]}', style: TextStyle(color: Colors.white70)),
              ],
            ), flex: 4,)
          ],)
        ],
      )
      // 여기에 추가적인 위젯을 정의하여 상세 정보를 표시할 수 있습니다.
    );
  }
}