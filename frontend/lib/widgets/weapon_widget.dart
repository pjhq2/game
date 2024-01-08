import 'dart:convert';
import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:frontend/models/weapon_model.dart';

class WeaponWidget extends StatelessWidget {
  final WeaponModel weapon;

  WeaponWidget({required this.weapon});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(20),
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
              Text('${weapon.name}', style: TextStyle(color: Colors.yellowAccent, fontWeight: FontWeight.w700),),
              Text('(+${weapon.reinLevel})', style: TextStyle(color: Colors.white70))
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
                Text('최소데미지', style: TextStyle(color: Colors.white70)),
                Text('최대데미지', style: TextStyle(color: Colors.white70)),
                Text('무기데미지', style: TextStyle(color: Colors.white70))
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
                Text('${weapon.minDamage}(+${weapon.reinMinDamage})', style: TextStyle(color: Colors.white70)),
                Text('${weapon.maxDamage}(+${weapon.reinMaxDamage})', style: TextStyle(color: Colors.white70)),
                Text('${weapon.finalMinDamage} - ${weapon.finalMaxDamage}', style: TextStyle(color: Colors.white70))
              ],
            ), flex: 4,)
          ],)
        ],
      )
      // 여기에 추가적인 위젯을 정의하여 상세 정보를 표시할 수 있습니다.
    );
  }
}