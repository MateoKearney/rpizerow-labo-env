#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/kthread.h>
#include <linux/sched.h>
#include <linux/delay.h>
#include <linux/sched/signal.h>

// Variables globales para kernel threads
static struct task_struct *kthread_1 = NULL;
static struct task_struct *kthread_2 = NULL;

// TODO:
// Funciones para los hilos
static int hilo_1(void *params) {
	// Creacion de variables

	// Bucle mientras que la tarea no sea detenida
	while(!kthread_should_stop()) {
		printk("Kearney_Mateo_ej02: Hola desde el Hilo N°1");
		msleep(1000);
	}
	// Finalizacion del hilo
	return 0;
}
static int hilo_2(void *params) {
	// Creacion de variables

	// Bucle mientras que la tarea no sea detenida
	while(!kthread_should_stop()) {
		printk("Kearney_Mateo_ej02: Hola desde el Hilo N°2");
		msleep(1000);
	}
	// Finalizacion del hilo
	return 0;
}
/**
 * @brief Se llama cuando se carga en el kernel
*/
static int __init ej02_module_init(void) {
	// TODO:
	// - Crear ambos hilos
	// - Verificar que se hayan podido crear
	// - Correr hilos
	kthread_1 = kthread_create(hilo_1, NULL, "kthread_1");
    if(kthread_1 == NULL) {
        printk(KERN_INFO "Kearney_Mateo_ej02: No se pudo hacer el Primer Hilo");
		return -1;
    }

    kthread_2 = kthread_create(hilo_2, NULL, "kthread_2");
    if(kthread_2 == NULL) {
        printk(KERN_INFO "Kearney_Mateo_ej02: No se pudo hacer el Segundo Hilo");
		return -1;
    }
	wake_up_process(kthread_1);
	wake_up_process(kthread_2);

	return 0;
}

/**
 * @brief Se llama cuando se retira del kernel
*/
static void __exit ej02_module_exit(void) {
	// TODO:
	kthread_stop(kthread_1);
	kthread_stop(kthread_2);
	// - Detener hilos
}

// Registro funciones de inicializacion y salida
module_init(ej02_module_init);
module_exit(ej02_module_exit);

// Informacion del modulo (completar lo que corresponda)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("");
MODULE_DESCRIPTION("");
