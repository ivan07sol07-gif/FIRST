class Threat:
    def __init__(self, description, zone):
        self.description = description
        self.zone = zone
        self.level = 1

    def info(self):
        print("Опис:", self.description)
        print("Зона:", self.zone)
        print("Рівень:", self.level)

    def escalate(self):
        if self.level < 5:
            self.level += 1


class CyberThreat(Threat):
    def escalate(self):
        if self.level <= 3:
            self.level += 2
        else:
            self.level = 5


class PhysicalThreat(Threat):
    def escalate(self):
        if self.level < 5:
            self.level += 1


class Scanner:
    def __init__(self):
        pass

    def analyze_text(self, text, zone):

        if "вірус" in text:
            return CyberThreat(text, zone)
        if "хакер" in text:
            return CyberThreat(text, zone)
        if "пожежа" in text:
            return PhysicalThreat(text, zone)
        if "проникнення" in text:
            return PhysicalThreat(text, zone)

        return Threat(text, zone)


class ThreatLog:
    def __init__(self):
        self.threats = []
        self.total_count = 0

    def add_threat(self, threat_obj):
        self.threats.append(threat_obj)
        self.total_count += 1

    def print_report(self):

        for element in self.threats:
            element.info()
            print(element.__dict__)

        print("Всього загроз:", self.total_count)


if __name__ == "__main__":

    log = ThreatLog()
    scanner = Scanner()


    t1 = scanner.analyze_text("Виявлено комп'ютерний вірус", "Зона А")
    log.add_threat(t1)

    t2 = scanner.analyze_text("Пожежа на складі", "Зона Б")
    log.add_threat(t2)

    t3 = scanner.analyze_text("Якась невідома подія", "Зона В")
    log.add_threat(t3)


    t1.escalate()
    t2.escalate()
    t3.escalate()


    if isinstance(t1, CyberThreat):
        setattr(t1, "status", "CRITICAL")

    
    log.print_report()