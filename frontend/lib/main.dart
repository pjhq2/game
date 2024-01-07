import 'package:flutter/material.dart';
import 'package:frontend/screens/home.dart';
import 'package:frontend/models/weapon.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Weapon(),
    );
  }
}