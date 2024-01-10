import 'dart:convert';
import 'dart:html';

import 'package:flutter/material.dart';
import 'package:frontend/models/inventory_model.dart';

class InventoryWidget extends StatelessWidget {
  final InventoryModel inventory;

  InventoryWidget({required this.inventory});

  @override
  Widget build(BuildContext context) {
    print(inventory.itemList[0]['이름']);
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
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(child: Text('장비', style: TextStyle(fontWeight: FontWeight.w700),),),
              Container(child: Text('소비', style: TextStyle(fontWeight: FontWeight.w700),),),
              Container(child: Text('기타', style: TextStyle(fontWeight: FontWeight.w700),),),
              Container(child: Text('캐시', style: TextStyle(fontWeight: FontWeight.w700),),),
            ],
          ),
          Column(
            children: inventory.itemList.map((item) => item!=null ? Text(item['이름'], style: TextStyle(color: Colors.white70),) : Text('null')).toList()
          ),
      ],)
      // 여기에 추가적인 위젯을 정의하여 상세 정보를 표시할 수 있습니다.
    );
  }
}