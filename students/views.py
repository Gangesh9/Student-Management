from rest_framework import generics
from .models import Student, Mark
from .serializers import StudentSerializer, MarkSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

class MarkCreateView(generics.CreateAPIView):
    serializer_class = MarkSerializer

    def perform_create(self, serializer):
        student = Student.objects.get(pk=self.kwargs['pk'])
        serializer.save(student=student)

class MarkListView(generics.ListAPIView):
    serializer_class = MarkSerializer

    def get_queryset(self):
        student = Student.objects.get(pk=self.kwargs['pk'])
        return Mark.objects.filter(student=student)

class StudentResultsView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        students = Student.objects.all()
        grade_counts = {'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        total_students = 0
        pass_count = 0

        for student in students:
            total_students += 1
            marks = Mark.objects.filter(student=student)
            if marks:
                total_mark = sum(m.score for m in marks) / len(marks)
                if total_mark >= 91:
                    grade_counts['S'] += 1
                elif total_mark >= 81:
                    grade_counts['A'] += 1
                elif total_mark >= 71:
                    grade_counts['B'] += 1
                elif total_mark >= 61:
                    grade_counts['C'] += 1
                elif total_mark >= 51:
                    grade_counts['D'] += 1
                elif total_mark >= 50:
                    grade_counts['E'] += 1
                else:
                    grade_counts['F'] += 1
            else:
                grade_counts['F'] += 1

        pass_count = total_students - grade_counts['F']
        pass_percentage = (pass_count / total_students) * 100

        print(f"S grade: {grade_counts['S']}")
        print(f"A grade: {grade_counts['A']}")
        print(f"B grade: {grade_counts['B']}")
        print(f"C grade: {grade_counts['C']}")
        print(f"D grade: {grade_counts['D']}")
        print(f"E grade: {grade_counts['E']}")
        print(f"F grade: {grade_counts['F']}")
        print(f"Pass percentage: {pass_percentage}")

        return students
