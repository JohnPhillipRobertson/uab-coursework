package cs.mad.habittracker.adapters

import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import cs.mad.habittracker.entities.Habit
import cs.mad.habittracker.entities.HabitDao
import kotlinx.coroutines.CoroutineScope

class HabitEntitiesAdapter(dataSet: List<Habit>, scope: CoroutineScope, dao: HabitDao) {//: RecyclerView.Adapter<HabitEntitiesAdapter.ViewHolder>() {

    private val dataSet = mutableListOf<Habit>()
    private val scope = scope
    private val dao = dao

    init {
        this.dataSet.addAll(dataSet)
    }

    /*override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): HabitEntitiesAdapter.ViewHolder {
        TODO("Not yet implemented")
    }*/


}