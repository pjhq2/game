import 'package:flutter/material.dart';
import 'package:frontend/models/weapon_model.dart'; // WeaponModel 임포트

class WeaponWidget extends StatelessWidget {
  final WeaponModel weapon;

  WeaponWidget({required this.weapon});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4.0,
      margin: EdgeInsets.all(8.0),
      child: ListTile(
        leading: Icon(Icons.gamepad), // 예시 아이콘
        title: Text(weapon.name),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Type: ${weapon.type}'),
            Text('Grade: ${weapon.gradeName}'),
            // 추가 필드를 여기에 추가할 수 있습니다.
          ],
        ),
        // 여기에 추가적인 위젯을 정의하여 상세 정보를 표시할 수 있습니다.
        // 예: onTap 이벤트를 사용하여 상세 화면으로 이동하는 기능을 구현할 수 있습니다.
        onTap: () {
          // 상세 화면으로 이동하는 기능 구현
        },
      ),
    );
  }
}