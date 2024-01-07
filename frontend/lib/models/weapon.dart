import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Weapon extends StatefulWidget {
  const Weapon({super.key});

  @override
  State<Weapon> createState() => _WeaponState();
}

class _WeaponState extends State<Weapon> {
  dynamic weaponInfo = {'이름': '이이', '등급': '3'};
  @override
  Widget build(BuildContext context) {
    final id = weaponInfo['id'];
    final name = weaponInfo['이름'];
    final grade = weaponInfo['등급'].toString();
    final reinlevel = weaponInfo['강화레벨'].toString();
    final header = name + '(+' + grade + ')';
    return Scaffold(
      appBar: AppBar(
          title: const Text('Rest API Weapon Call')
      ),
      body: Column(
        children: [
          Text(header),
          Text(grade),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: fetchWeaponInfo,
      ),);
  }

  void fetchWeaponInfo() async {
    print('fetchWeaponInfo called');
    const url = 'http://127.0.0.1:8000/api/v1/';
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.bodyBytes;
    final json = jsonDecode(utf8.decode(body));
    print(json);
    setState(() {
      weaponInfo = json;
    });
    print('fetch completed');
  }
}
