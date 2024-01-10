import 'package:flutter/material.dart';
import 'package:frontend/models/weapon_model.dart';
import 'package:frontend/services/test_service.dart';
import 'package:frontend/widgets/weapon_widget.dart';

class TestScreen extends StatefulWidget {
  const TestScreen({super.key});

  @override
  State<TestScreen> createState() => _TestScreenState();
}

class _TestScreenState extends State<TestScreen> {
  late Future<WeaponModel> futureWeaponData;

  @override
  void initState() {
    super.initState();
    futureWeaponData = TestService().fetchWeaponData();
  }

  Widget build(BuildContext context) {
    return Container(
      width: 100,
      height: 100,
      color: Colors.blue,
      child: FutureBuilder(
        future: futureWeaponData,
        builder: (context, snapshot){
          return GestureDetector(
              onTap: (){
                setState(() {
                  futureWeaponData = TestService().fetchWeaponData();
                });
              },
              child: Text('${snapshot.data}')
              // child: WeaponWidget(weapon: snapshot.data!),  // '!' 붙이면 뭔가 알아서 맞춰서 json 내부꺼 끼워주는 느낌?
            );      }
      ),
    );
  }
}
