import 'package:flutter/material.dart';
// Models
import 'package:frontend/models/weapon_model.dart';
// Screens
import 'package:frontend/screens/screen_home.dart';
import 'package:frontend/screens/screen_weapon.dart';
import 'package:frontend/screens/screen_test.dart';
import 'package:frontend/screens/screen_inventory.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weapon App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: InventoryScreen(),
      // home: WeaponScreen(),
      // home: TestScreen(),
    );
  }
}