import 'package:flutter/material.dart';
<<<<<<< HEAD
// Models
import 'package:frontend/models/weapon_model.dart';
// Screens
import 'package:frontend/screens/screen_home.dart';
import 'package:frontend/screens/screen_weapon.dart';

=======
import 'package:frontend/screen/home.dart';
>>>>>>> parent of e058dce (weapon model temp)

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
    return MaterialApp(
      title: 'Weapon App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: WeaponScreen(),
=======
    return const MaterialApp(
      home: HomeScreen(),
>>>>>>> parent of e058dce (weapon model temp)
    );
  }
}