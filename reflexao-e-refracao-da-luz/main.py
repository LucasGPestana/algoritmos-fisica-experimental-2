from src.refractive_module import RefractiveModule

if __name__ == "__main__":

  N_AR = 1.0003
  ANGULO_INCIDENCIA_INICIAL = 10
  
  mod1 = RefractiveModule(N_AR, "AR")

  mod1.setIncidenceThetas(ANGULO_INCIDENCIA_INICIAL, 8)
  mod1.setRefractionThetas([7, 13, 19, 25, 31, 35, 39, 41])

  mod1.generateReport("módulo 1")

  mod2 = RefractiveModule(N_AR, "ACRILICO")

  mod2.setIncidenceThetas(ANGULO_INCIDENCIA_INICIAL, 4)
  mod2.setRefractionThetas([15, 31, 48, 73])

  mod2.generateReport("módulo 2")

  mod3 = RefractiveModule(N_AR, "ACRÍLICO")

  mod3.setIncidenceThetas(43, 1)
  mod3.setRefractionThetas([90])

  mod3.generateReport("ângulo crítico")


