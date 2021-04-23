package cs.mad.habittracker.adapters

import android.annotation.SuppressLint
import android.graphics.Color.RED
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import cs.mad.habittracker.databinding.ItemStatBinding
import cs.mad.habittracker.entities.Habit
import cs.mad.habittracker.entities.HabitDao
import java.util.*

class StatsAdapter(private var dataSet: List<Habit>, private val dao: HabitDao) :
        RecyclerView.Adapter<StatsAdapter.ViewHolder>() {

    init {
        setData(dataSet)
    }

    /**
     * Provide a reference to the type of views that you are using
     * (custom ViewHolder).
     */
    class ViewHolder(bind: ItemStatBinding) : RecyclerView.ViewHolder(bind.root) {
        val binding: ItemStatBinding = bind
    }

    // Create new views (invoked by the layout manager)
    override fun onCreateViewHolder(viewGroup: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemStatBinding.inflate(
                LayoutInflater.from(viewGroup.context),
                viewGroup,
                false
        )
        binding.root.minimumHeight = viewGroup.height / 4
        return ViewHolder(binding)
    }

    // Replace the contents of a view (invoked by the layout manager)
    @SuppressLint("SetTextI18n")
    override fun onBindViewHolder(viewHolder: ViewHolder, position: Int) {
        val item = dataSet[position]
        val goal = item.goal.toFloat()
        val dateCreated = item.date_created
        val interval = item.interval
        val timesPerformed = item.timesPerformed.toFloat()

        var stat = 0.toFloat()

        // date logic
        val now = Calendar.getInstance().timeInMillis
        val daysTracked = ((now - dateCreated) / (1000 * 60 * 60 * 24)).toInt()  // 1000 milli per second, 60 sec per min, 60 min per hour, 24 hours per day


        if (daysTracked == 0) {
            stat = (timesPerformed / goal) * 100
        }
        else {
            if (interval === "daily") {
                stat = (timesPerformed/ (goal * daysTracked)) * 100
            } else if (interval === "weekly") {
                stat = (timesPerformed / (goal * (daysTracked / 7))) * 100
            }
        }

        if (stat < 100) {
            viewHolder.binding.cardBackground.setCardBackgroundColor(RED)
        }
        viewHolder.binding.statName.text = item.name
        viewHolder.binding.statGoal.text = "Goal: ${goal.toInt()} $interval"
        viewHolder.binding.timesCompleted.text = "Completed ${item.timesPerformed} times"
        viewHolder.binding.statPercent.text = "$stat%"
        viewHolder.binding.daysTrackedLabel.text = "Days Tracked: $daysTracked"
    }

    override fun getItemCount(): Int {
        return dataSet.size
    }

    fun setData(items: List<Habit>) {
        dataSet = items
        notifyDataSetChanged()
    }
}