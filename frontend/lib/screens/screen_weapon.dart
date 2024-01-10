import 'package:flutter/material.dart';
import 'package:frontend/models/weapon_model.dart';
import 'package:frontend/services/weapon_service.dart';
import 'package:frontend/widgets/weapon_widget.dart';

class WeaponScreen extends StatefulWidget {
  @override
  _WeaponScreenState createState() => _WeaponScreenState();
}

class _WeaponScreenState extends State<WeaponScreen> {
  late Future<List<WeaponModel>> futureWeapons;

  @override
  void initState() {
    super.initState();
    futureWeapons = WeaponService().fetchWeapons();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Weapon List'),
      ),
      body: SizedBox(
        width: 250,
        child: FutureBuilder<List<WeaponModel>>(
          future: futureWeapons,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(child: CircularProgressIndicator());
            } else if (snapshot.hasError) {
              return Center(child: Text('Error: ${snapshot.error}'));
            } else {
              return ListView.builder(
                itemCount: snapshot.data?.length ?? 0,
                itemBuilder: (context, index) {
                  return Container(
                    child: WeaponWidget(weapon: snapshot.data![index],),
                  );
                },
              );
            }
          },
        ),
      ),
    );
  }
}

class WeaponDetailScreen extends StatelessWidget {
  final WeaponModel weapon;

  WeaponDetailScreen({required this.weapon});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(weapon.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Type: ${weapon.type}'),
            Text('Grade: ${weapon.gradeName}'),
            // 추가적인 무기 정보 표시
          ],
        ),
      ),
    );
  }
}