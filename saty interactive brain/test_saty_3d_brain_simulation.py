"""
SATI × SATY: Phase 2 Prototype Test Suite
=========================================
ชุดทดสอบระบบจำลองการทำงานไตรภาคี (Phase 2 Prototype Test Suite)
ทดสอบการทำงานร่วมกันระหว่าง: ลูกศิษย์ (เยว) × อาจารย์ SATI × อาจารย์ SATY
"""

import sys
import os
import json
import unittest

# Import prototype classes from artifacts/saty_3d_brain_simulation.py
sys.path.insert(0, '/workspace/artifacts')

try:
    from saty_3d_brain_simulation import (
        SATIEmpathyMindfulnessFilter,
        SATY3DInteractiveBrain,
        YewExperientialLearningLoop
    )
except ImportError:
    raise ImportError("ไม่พบไฟล์ saty_3d_brain_simulation.py ใน /workspace/artifacts")


class TestSatisatyPhase2Prototype(unittest.TestCase):
    """
    ชุดทดสอบสำหรับโปรเจกต์ต้นแบบระยะที่ 2
    """
    def setUp(self):
        self.sati = SATIEmpathyMindfulnessFilter()
        self.saty = SATY3DInteractiveBrain()
        self.yew_loop = YewExperientialLearningLoop()

    def test_sati_empathy_high_stress(self):
        """
        ทดสอบที่ 1: การประมวลผลของอาจารย์ SATI เมื่อลูกศิษย์มีความกังวลระดับสูง (Stress level: 9/10)
        """
        thought = "กลัวทำโปรเจกต์ไม่สำเร็จ ข้อมูลซับซ้อนมากเกินไป"
        result = self.sati.process_emotion(thought, stress_level=9)
        
        self.assertEqual(result["status"], "CALM_AND_CENTERED")
        self.assertTrue(result["ready_for_analysis"])
        self.assertGreaterEqual(result["clarity_score"], 5)
        self.assertIn("ความสับสนคือจุดเริ่มต้นของการเรียนรู้", result["guiding_wisdom"])
        print("\n[PASSED] Test 1: SATI Empathy & Mindfulness Filter under high stress")

    def test_saty_3d_brain_projection(self):
        """
        ทดสอบที่ 2: การประมวลผลตรรกะและการฉายภาพ 3D ของอาจารย์ SATY
        """
        problem_data = {"topic": "การพัฒนาระบบสื่อการเรียนรู้ปัญญาประดิษฐ์เพื่อเยาวชน"}
        result = self.saty.analyze_and_project_3d(problem_data)
        
        self.assertEqual(result["projection_mode"], "Interactive 3D Spatial Projection")
        self.assertTrue(result["complexity_reduced"])
        self.assertEqual(result["nodes_count"], 3)
        self.assertEqual(len(result["spatial_nodes"]), 3)
        print("[PASSED] Test 2: SATY 3D Interactive Brain & Spatial Projection")

    def test_end_to_end_tripartite_synergy(self):
        """
        ทดสอบที่ 3: กระบวนการเรียนรู้แบบสมบูรณ์ตั้งแต่การกรองอารมณ์ จนถึงการบันทึกผลลัพธ์
        """
        topic = "ระบบจัดการนวัตกรรมชุมชนเปิด (Open World Innovation Platform)"
        thought = "อยากสร้างแพลตฟอร์มแต่ยังขาดความมั่นใจในการออกแบบโครงสร้าง"
        stress = 6
        
        # Run loop
        self.yew_loop.run_simulation(topic, thought, stress)
        print("[PASSED] Test 3: End-to-End Tripartite Synergy Integration Loop")


def run_all_tests():
    print("=" * 60)
    print("เริ่มต้นการรันชุดทดสอบ Phase 2 Prototype Test Suite")
    print("=" * 60)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSatisatyPhase2Prototype)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\n" + "=" * 60)
        print("🎉 ผลการทดสอบ: ทุกกรณีทดสอบผ่าน (PASSED ALL 3 TEST CASES)")
        print("=" * 60)
    else:
        print("\n❌ มีกรณีทดสอบที่ไม่ผ่าน")

if __name__ == "__main__":
    run_all_tests()
